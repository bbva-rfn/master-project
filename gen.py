import numpy as np
from Graph import Graph
from Node import *

num_nodes = 1000
num_sectors = 17
approx_num_connections = 10
defaulted_prob = 0.01

nodes = []
for _ in range(num_nodes):
    node = Node()
    node.set_feature('defaulted', np.random.choice([0, 1], p=[1 - defaulted_prob, defaulted_prob]))
    node.set_feature('sector', np.random.randint(num_sectors))
    nodes.append(node)

nodes = np.array(nodes)

graph = Graph(nodes)

for node_id in range(graph.num_nodes):
    num_connections = min(np.random.poisson(approx_num_connections), graph.num_nodes - 1)
    connections = np.random.choice(range(graph.num_nodes), num_connections, replace=False)
    graph.set_connections(node_id, connections)

    node = nodes[node_id]
    node.set_feature('all_connected', connections)
    weights = 1 / num_connections
    # weights = np.random.beta(2, 5, num_connections)
    # weights /= np.sum(weights)
    node.set_feature('weights', weights)

graph.save('graphs/test.pickle')
