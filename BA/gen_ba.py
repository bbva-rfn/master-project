import pickle
import networkx as nx
import numpy as np

num_nodes = 1000
num_sectors = 5
num_connections_entry = 3 #each node enters with 3
defaulted_prob = 0.01



graph = nx.barabasi_albert_graph(num_nodes,num_connections_entry)

graph_final = nx.DiGraph()

all_node_ids = range(num_nodes)

already_considered_pairs = []

for node_id in all_node_ids:
    #node = graph.nodes[node_id]
    neighbors = graph.neighbors(node_id)
    aux = 1
    connected_node_ids = []
    #num_to_directed = len(neighbors)/2
    for nei in neighbors:
        connected_node_ids.append(nei)
    
    num_connections = len(connected_node_ids)
    weights_val = 1 / num_connections
    weighted_edges = [(node_id, to_node_id, weights_val) for to_node_id in connected_node_ids]

    node_attrs = {
        'id': node_id,
        'defaulted': np.random.choice([0., 1.], p=[1 - defaulted_prob, defaulted_prob]),
        'total_defaulted_turns': 0,
        'first_defaulted_at': -1,
        'sector': np.random.randint(num_sectors),
        'all_connected_nodes': connected_node_ids
    }

    graph_final.add_node(node_id, **node_attrs)
    graph_final.add_weighted_edges_from(weighted_edges)

pickle.dump(graph_final, open('graph_ba.pickle', 'wb'))