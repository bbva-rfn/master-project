import numpy as np
from nptyping import Array

from Graph import Graph
from Node import Node

# Parameters, modifiable
iterations = 100
beta = 0.3

# Load in graph
graph = Graph.load('graphs/test.pickle')


# Algorithm


def get_nodes_per_sector(graph):
    nodes_per_sector = {}

    for node_id in range(graph.num_nodes):
        node = graph.get_nodes(node_id)

        sector = node.get_feature('sector')
        if sector in nodes_per_sector:
            nodes_per_sector[sector] = np.append(nodes_per_sector[sector], node_id)
        else:
            nodes_per_sector[sector] = np.array([node_id])

    return nodes_per_sector


def calculate_q(nodes: Array[Node], r):
    defaulted_probs = []
    for node in nodes:
        defaulted_probs.append(node.get_feature('defaulted'))

    defaulted_probs = np.array(defaulted_probs)
    return np.prod(1 - beta * r * defaulted_probs)


defaulted_density = []
nodes_per_sector = get_nodes_per_sector(graph)


def update_default(node: Node, graph: Graph):
    defaulted_p = node.get_feature('defaulted')
    r = node.get_feature('weights')
    connected_nodes = graph.get_connected_nodes(node.id)

    q = calculate_q(connected_nodes, r)
    new_defaulted_p = np.clip((1 - q) * (1 - defaulted_p), 0., 1.)

    all_connected_nodes = node.get_feature('all_connected')

    for connected_node in connected_nodes:
        if connected_node.get_feature('defaulted') > defaulted_p:
            graph.remove_connections(node.id, connected_node.id)
            sector = connected_node.get_feature('sector')
            nodes_in_sector = nodes_per_sector[sector]
            not_in_connected_mask = np.isin(nodes_in_sector, all_connected_nodes, invert=True)
            eligible_nodes = graph.get_nodes(nodes_in_sector[not_in_connected_mask])
            eligible_nodes = np.array([node for node in eligible_nodes if node.get_feature('defaulted') <= defaulted_p])

            if eligible_nodes.size == 0:
                new_weights = node.get_feature('weights')[:-1]
                node.set_feature('weights', new_weights)
                continue

            new_node = np.random.choice(eligible_nodes)
            graph.set_connections(node.id, new_node.id)
            all_connected_nodes = np.append(all_connected_nodes, new_node.id)
            node.set_feature('all_connected', all_connected_nodes)

    node.set_feature('defaulted', new_defaulted_p)


def iteration(graph: Graph):
    total_p = 0

    for node_id in range(graph.num_nodes):
        node = graph.get_nodes(node_id)
        total_p += node.get_feature('defaulted')
        update_default(node, graph)

    cur_density = total_p / graph.num_nodes
    defaulted_density.append(cur_density)


for i in range(iterations):
    iteration(graph)
    print(defaulted_density[-1], i)

