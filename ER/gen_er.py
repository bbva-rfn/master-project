import pickle
import networkx as nx
import numpy as np

num_nodes = 1000
num_sectors = 5
defaulted_prob = 0.01

edge_prob = 0.004 #this gives arrund 5 edges per node

graph = nx.erdos_renyi_graph(num_nodes,edge_prob,directed=True)

'''
This checks on screen that in general you are not a neighbor of your neighbor i.e. directed nice

for node_id in [1]:
    neigh = graph.neighbors(node_id)
    for n in neigh:
        print('\nNeighbor',n)
        nei = graph.neighbors(n)
        print('Neighbors of %s'%n)
        for nn in nei:
            print(nn)
            
'''
print(graph.number_of_edges())
#we check if this number is close to the 3000 from the barabasi albert one for comparison

graph_final = nx.DiGraph()

all_node_ids = range(num_nodes)

already_considered_pairs = []

for node_id in all_node_ids:
    
    neighbors = graph.neighbors(node_id)
    connected_node_ids = []
    
    for nei in neighbors:
        connected_node_ids.append(nei)
    
    num_connections = len(connected_node_ids)
    
    if num_connections!=0:
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

print(graph_final.number_of_nodes())
pickle.dump(graph_final, open('graph_er.pickle', 'wb'))
