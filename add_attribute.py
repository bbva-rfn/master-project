import pickle

name = 'BBVA/bbva'

g = pickle.load(open(name + '.pickle', 'rb'))

for node_id in g:
    in_conn = [edge[0] for edge in g.in_edges(node_id)]
    node = g.nodes[node_id]
    node['all_connected_nodes_in'] = in_conn

pickle.dump(g, open(name + '.pickle', 'wb'))