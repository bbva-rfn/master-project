import numpy as np

from Graph import Graph
from Node import Node

nodes = []
for _ in range(100):
    node = Node()
    nodes.append(node)

nodes = np.array(nodes)

graph = Graph(nodes)

for node_id in range(graph.num_nodes):
    num_connections = min(np.random.poisson(10), graph.num_nodes - 1)
    connections = np.random.choice(range(graph.num_nodes), num_connections, replace=False)
    graph.set_connections(node_id, connections)

