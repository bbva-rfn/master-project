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


class SecNetSimple:
    def __init__(self, graph: DiGraph, mu: float, beta: float):
        self.graph = graph.copy()

        self.mu = mu
        self.beta = beta
        self.defaulted_density = []

    def plot(self):
        fig = figure()
        ax = fig.add_subplot(111)
        ax.plot(self.defaulted_density)
        show()

    def run(self, iterations=100, verbose=True):
        if verbose:
            print()

        for it in range(iterations):
            if verbose:
                print_progress(it + 1, iterations)
            self.iterate()

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

    def calculate_p(self, defaulted_p, neighbor_nodes, weights):
        mu = self.mu
        q = self.calculate_q(neighbor_nodes, weights)

        new_p = (1 - q) * (1 - defaulted_p) + (1 - mu) * defaulted_p + mu * (1 - q) * defaulted_p
        new_p = 1 if np.random.random() < new_p else 0

        return new_p

    def calculate_q(self, nodes, weights):
        # r = 0

        defaulted_probs = []
        for node in nodes:
            defaulted_probs.append(node['defaulted'])
            # r += 1

        # print(weights)
        # weights = 1. / r

        defaulted_probs = np.array(defaulted_probs)
        return np.prod(1 - self.beta * weights * defaulted_probs)
