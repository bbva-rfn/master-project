import pickle
import networkx as nx
import numpy as np


num_nodes = 1000

sectors = {
    'Financial Institutions': {
        'size': 0.00046,
        'in': 39.613,
        'out': 45.529,
        'default': 0.03650,
    },
    'Energy': {
        'size': 0.00083,
        'in': 12.844,
        'out': 8.666,
        'default': 0.01111,
    },
    'Financial Services': {
        'size': 0.01165,
        'in': 6.300,
        'out': 20.265,
        'default': 0.00786,
    },
    'Utilities': {
        'size': 0.01529,
        'in': 5.589,
        'out': 5.903,
        'default': 0.01264,
    },
    'Telecom': {
        'size': 0.03299,
        'in': 5.960,
        'out': 5.194,
        'default': 0.01776,
    },
    'Basic Materials': {
        'size': 0.02745,
        'in': 5.789,
        'out': 5.350,
        'default': 0.02782,
    },
    'Transportation': {
        'size': 0.04064,
        'in': 5.411,
        'out': 4.336,
        'default': 0.01868,
    },
    'Retail': {
        'size': 0.23593,
        'in': 3.973,
        'out': 3.233,
        'default': 0.01217,
    },
    'Capital Goods': {
        'size': 0.08689,
        'in': 4.528,
        'out': 3.098,
        'default': 0.01866,
    },
    'Auto': {
        'size': 0.0147,
        'in': 4.454,
        'out': 2.991,
        'default': 0.01786,
    },
    'Consumer and Healthcare': {
        'size': 0.07055,
        'in': 3.259,
        'out': 3.770,
        'default': 0.01539,
    },
    'Construction and Infrastructure': {
        'size': 0.08907,
        'in': 3.067,
        'out': 3.270,
        'default': 0.03071,
    },
    'Unknown': {
        'size': 0.10159,
        'in': 0.930,
        'out': 1.413,
        'default': 0.01942,
    },
    'Real Estate': {
        'size': 0.0843,
        'in': 1.517,
        'out': 1.833,
        'default': 0.03603,
    },
    'Leisure': {
        'size': 0.12861,
        'in': 2.509,
        'out': 2.512,
        'default': 0.01511,
    },
    'Institutions': {
        'size': 0.03219,
        'in': 5.547,
        'out': 10.764,
        'default': 0.535,
    }
}

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
