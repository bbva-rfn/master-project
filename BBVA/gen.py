import pickle
import networkx as nx
import numpy as np
from sectors import sectors

num_nodes = 10000

graph = nx.DiGraph()

in_conn_ratios = []
nodes_per_sector = {}

for sector, data in sectors.items():
    num_nodes_sector = round(num_nodes * data['size'])
    node_ids = range(graph.number_of_nodes(), graph.number_of_nodes() + num_nodes_sector)
    graph.add_nodes_from(node_ids, sector=sector)
    in_conn_ratios.append(data['in'] * data['size'])
    nodes_per_sector[sector] = node_ids

in_conn_ratios = [el / sum(in_conn_ratios) for el in in_conn_ratios]


def get_connections(node_id, num_connections):
    rand_sectors = np.random.choice([*sectors], num_connections, p=in_conn_ratios)
    rand_node_ids = []
    for rs in rand_sectors:
        rand_node_id = np.random.choice(nodes_per_sector[rs])
        while rand_node_id == node_id:
            rand_node_id = np.random.choice(nodes_per_sector[rs])

        rand_node_ids.append(rand_node_id)

    return rand_node_ids


for node_id in graph.nodes:
    node = graph.nodes[node_id]
    sector = node['sector']
    sector_data = sectors[sector]
    defaulted_prob = sector_data['default']

    num_connections = max(1, round(np.random.normal(sector_data['out'])))
    connected_node_ids = get_connections(node_id, num_connections)

    weights_val = 1 / num_connections
    weighted_edges = [(node_id, to_node_id, weights_val) for to_node_id in connected_node_ids]

    node_attrs = {
        'id': node_id,
        'defaulted': np.random.choice([0., 1.], p=[1 - defaulted_prob, defaulted_prob]),
        'total_defaulted_turns': 0,
        'first_defaulted_at': -1,
        'all_connected_nodes': connected_node_ids
    }

    graph.add_node(node_id, **node_attrs)
    graph.add_weighted_edges_from(weighted_edges)

pickle.dump(graph, open('bbva.pickle', 'wb'))
