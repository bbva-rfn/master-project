import pickle
import networkx as nx
import numpy as np

num_nodes = 1000
num_sectors = 17
approx_num_connections = 10
defaulted_prob = 0.01

graph = nx.DiGraph()

all_node_ids = range(num_nodes)

for node_id in all_node_ids:
    num_connections = np.clip(np.random.poisson(approx_num_connections), 1, num_nodes - 1)
    accepted_node_ids = list(filter(lambda idx: idx != node_id, all_node_ids))  # avoid self-looping
    connected_node_ids = np.random.choice(accepted_node_ids, num_connections, replace=False)

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

    graph.add_node(node_id, **node_attrs)
    graph.add_weighted_edges_from(weighted_edges)

pickle.dump(graph, open('graphs/new.pickle', 'wb'))
