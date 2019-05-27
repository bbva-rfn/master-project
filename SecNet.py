import sys
from enum import Enum

import numpy as np
from matplotlib.pyplot import show, figure
from networkx import DiGraph, set_node_attributes


def print_progress(current, total, num_bars=40):
    fraction = current / total
    percentage = int(100 * fraction)
    num_hashtags = int(fraction * num_bars)

    progress_bar = "#" * num_hashtags + "_" * (num_bars - num_hashtags)
    sys.stdout.write("\033[F")
    print("[%s] %d%%" % (progress_bar, percentage))


class ReconnectionPolicy(Enum):
    NONE = 1
    RANDOM = 2
    SOFT = 3
    STRONG = 4


class SecNet:
    def __init__(self, graph: DiGraph, mu: float, beta: float, stochastic: bool = True,
                 reconnection_policy: ReconnectionPolicy = ReconnectionPolicy.NONE,
                 default_delay=0):
        self.graph = graph.copy()

        self.mu = mu
        self.beta = beta
        self.stochastic = stochastic
        self.reconnection_policy = reconnection_policy
        self.default_delay = default_delay

        self.defaulted_density = []
        self.nodes_per_sector = self.get_nodes_per_sector()

        if default_delay != 0:
            self.init_default_delay()

    def init_default_delay(self):
        set_node_attributes(self.graph, 0, name='defaulted_turns')

    def run(self, iterations=100, verbose=True):
        if verbose:
            print()

        for it in range(iterations):
            if verbose:
                print_progress(it + 1, iterations)
            self.iterate()

    def plot(self):
        fig = figure()
        ax = fig.add_subplot(111)
        ax.plot(self.defaulted_density)
        show()

    def iterate(self):
        graph = self.graph
        total_p = 0

        for node_id in graph:
            node = graph.nodes[node_id]
            total_p += node['defaulted']
            self.update_default(node)

        cur_density = total_p / graph.number_of_nodes()
        self.defaulted_density.append(cur_density)

    def update_default(self, node):
        graph = self.graph

        defaulted_p = node['defaulted']
        neighbors = graph[node['id']]
        weights = np.array([neighbor['weight'] for neighbor in neighbors.values()])
        neighbor_nodes = [graph.nodes[node_id] for node_id in list(neighbors)]
        new_defaulted_p = self.calculate_p(defaulted_p, neighbor_nodes, weights)
        node['defaulted'] = new_defaulted_p

        self.reconnect_neighbors(node, neighbor_nodes)

    def reconnect_neighbors(self, node, neighbor_nodes):
        if self.reconnection_policy == ReconnectionPolicy.NONE:
            return None

        for neighbor in neighbor_nodes:
            if self.should_reconnect(node, neighbor, self.reconnection_policy):
                self.reconnect(node, neighbor)

    def reconnect(self, node, neighbor):
        graph = self.graph
        weight = graph[node['id']][neighbor['id']]['weight']
        graph.remove_edge(node['id'], neighbor['id'])
        eligible_nodes = self.get_reconnectable_nodes(node, neighbor)

        if eligible_nodes.size == 0:
            edges = graph[node['id']]
            self.normalize_edges(edges)
        else:
            new_node = np.random.choice(eligible_nodes)
            graph.add_edge(node['id'], new_node['id'], weight=weight)

            node['all_connected_nodes'] = np.append(node['all_connected_nodes'], new_node['id'])

    @staticmethod
    def normalize_edges(edges):
        weights = [edges[to_node_id]['weight'] for to_node_id in edges]
        sum_weights = np.sum(weights)
        for connected_node_id in edges:
            edges[connected_node_id]['weight'] /= sum_weights

    def get_reconnectable_nodes(self, node, neighbor):
        graph = self.graph
        policy = self.reconnection_policy
        sector = neighbor['sector']
        nodes_in_sector = self.nodes_per_sector[sector]
        all_connected_nodes = node['all_connected_nodes']
        defaulted_p = node['defaulted']

        not_in_connected_mask = np.isin(nodes_in_sector, all_connected_nodes, invert=True)
        if policy == ReconnectionPolicy.SOFT:
            eligible_nodes = [graph.nodes[node_id] for node_id in nodes_in_sector[not_in_connected_mask]
                              if graph.nodes[node_id]['defaulted'] <= node['defaulted']]
        elif policy == ReconnectionPolicy.STRONG:
            eligible_nodes = [graph.nodes[node_id] for node_id in nodes_in_sector[not_in_connected_mask]
                              if graph.nodes[node_id]['defaulted'] < node['defaulted']]
        else:
            eligible_nodes = [graph.nodes[node_id] for node_id in nodes_in_sector[not_in_connected_mask]]

        return np.array([node for node in eligible_nodes if node['defaulted'] <= defaulted_p])

    def calculate_p(self, defaulted_p, neighbor_nodes, weights):
        mu = self.mu
        q = self.calculate_q(neighbor_nodes, weights)

        new_p = (1 - q) * (1 - defaulted_p) + (1 - mu) * defaulted_p + mu * (1 - q) * defaulted_p
        new_p = self.apply_p_policy(new_p, self.stochastic)

        return new_p

    def should_reconnect(self, node, neighbor, reconnection_policy):
        wait = self.default_delay and neighbor['defaulted_turns'] < self.default_delay
        reconnect = False

        if reconnection_policy in [ReconnectionPolicy.SOFT, ReconnectionPolicy.RANDOM]:
            reconnect = neighbor['defaulted'] == 1

        if reconnection_policy == ReconnectionPolicy.STRONG:
            reconnect = neighbor['defaulted'] == 1 or neighbor['defaulted'] > node['defaulted']

        if reconnect and self.default_delay:
            neighbor['defaulted_turns'] += 1
            print(neighbor['defaulted_turns'])

        if not reconnect:
                neighbor['defaulted_turns'] = 0

        return reconnect and not wait

    @staticmethod
    def apply_p_policy(p, is_stochastic):
        if is_stochastic:
            return 1 if np.random.random() < p else 0

        return p

    def calculate_q(self, nodes, weights):
        defaulted_probs = []
        for node in nodes:
            defaulted_probs.append(node['defaulted'])

        defaulted_probs = np.array(defaulted_probs)
        return np.prod(1 - self.beta * weights * defaulted_probs)

    def get_nodes_per_sector(self):
        graph = self.graph
        nodes_per_sector = {}

        for node_id in graph:
            node = graph.nodes[node_id]

            sector = node['sector']
            if sector in nodes_per_sector:
                nodes_per_sector[sector] = np.append(nodes_per_sector[sector], node_id)
            else:
                nodes_per_sector[sector] = np.array([node_id])

        return nodes_per_sector
