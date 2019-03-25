import pickle

import matplotlib.animation as anim
import matplotlib.pyplot as plt
import numpy as np
from networkx import DiGraph

# Parameters, modifiable
iterations = 100
beta = 0.5
mu = 0.4

# Load in graph
graph = pickle.load(open('graphs/new.pickle', 'rb'))


# Algorithm

def get_nodes_per_sector(graph: DiGraph):
    nodes_per_sector = {}

    for node_id in graph:
        node = graph.nodes[node_id]

        sector = node['sector']
        if sector in nodes_per_sector:
            nodes_per_sector[sector] = np.append(nodes_per_sector[sector], node_id)
        else:
            nodes_per_sector[sector] = np.array([node_id])

    return nodes_per_sector


def calculate_q(nodes, weights):
    defaulted_probs = []
    for node in nodes:
        defaulted_probs.append(node['defaulted'])

    defaulted_probs = np.array(defaulted_probs)
    return np.prod(1 - beta * weights * defaulted_probs)


defaulted_density = []
nodes_per_sector = get_nodes_per_sector(graph)


def update_default(node, graph: DiGraph):
    defaulted_p = node['defaulted']
    neighbors = graph[node['id']]

    weights = np.array([neighbor['weight'] for neighbor in neighbors.values()])
    neighbor_nodes = [graph.nodes[node_id] for node_id in list(neighbors)]

    q = calculate_q(neighbor_nodes, weights)
    new_defaulted_p = (1 - q) * (1 - defaulted_p) + (1 - mu) * defaulted_p + mu * (1 - q) * defaulted_p
    # new_defaulted_p = np.clip(new_defaulted_p, 0, 1)
    # new_defaulted_p = defaulted_p if 0 > new_defaulted_p > 1 else new_defaulted_p
    new_defaulted_p = 1 if np.random.random() > new_defaulted_p else 0

    all_connected_nodes = node['all_connected_nodes']

    for weight, connected_node in zip(weights, neighbor_nodes):
        if connected_node['defaulted'] > defaulted_p:
            graph.remove_edge(node['id'], connected_node['id'])
            sector = connected_node['sector']
            nodes_in_sector = nodes_per_sector[sector]
            not_in_connected_mask = np.isin(nodes_in_sector, all_connected_nodes, invert=True)
            eligible_nodes = [graph.nodes[node_id] for node_id in nodes_in_sector[not_in_connected_mask]]
            eligible_nodes = np.array([node for node in eligible_nodes if node['defaulted'] <= defaulted_p])

            if eligible_nodes.size == 0:
                weights = [neighbor['weight'] for neighbor in neighbors.values()]
                sum_weights = np.sum(weights)
                updated_edges = [(node['id'], to_node_id, val['weight'] / sum_weights) for to_node_id, val in
                                 neighbors.items()]
                graph.update(edges=updated_edges)
                continue

            new_node = np.random.choice(eligible_nodes)
            graph.add_edge(node['id'], new_node['id'], weight=weight)
            all_connected_nodes = np.append(all_connected_nodes, new_node['id'])
            node['all_connected'] = all_connected_nodes

    node['defaulted'] = new_defaulted_p


def iteration(graph: DiGraph):
    total_p = 0

    for node_id in graph:
        node = graph.nodes[node_id]
        total_p += node['defaulted']
        update_default(node, graph)

    cur_density = total_p / graph.number_of_nodes()
    defaulted_density.append(cur_density)


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Iteration')
ax.set_ylabel('Defaulted probability density')


def update(_):
    iteration(graph)
    ax.clear()
    ax.set_xlabel('iteration')
    ax.set_ylabel('Defaulted probability density')
    ax.plot(defaulted_density)


a = anim.FuncAnimation(fig, update, frames=100, repeat=False)
plt.show()
