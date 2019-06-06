# -*- coding: utf-8 -*-
#adapting the code of cascades_old to the new general algorithm

from networkx import DiGraph
import pickle
from SecNet import SecNet, ReconnectionPolicy

#as we store at which iteration they become infected it is trivial
def cascade_origins(graph: DiGraph):
    origins = []
    for node_id in graph:
        node = graph.nodes[node_id]
        if node['first_defaulted_at'] == 0:
            origins.append(node_id)

    return origins


def check_infected_neighbours_recursive(graph: DiGraph, node_id, already_considered_nodes):   
    s = 0
    node = graph.nodes[node_id]
    neighbors = graph[node_id]
    neighbor_nodes = [graph.nodes[node_id] for node_id in list(neighbors)]
    for neighbor in neighbor_nodes:
        if neighbor['first_defaulted_at'] > node['first_defaulted_at']  and neighbor['id'] not in already_considered_nodes:
            already_considered_nodes.append(neighbor['id'])
            s += check_infected_neighbours_recursive(graph, neighbor['id'],already_considered_nodes)
            s += 1
            
    return s


def check_cascade_size_recursive(graph: DiGraph):
    origins = cascade_origins(graph)
    sizes = []
    already_considered_nodes = []
    for origin in origins:
        already_considered_nodes.append(origin)
        sizes.append(check_infected_neighbours_recursive(graph, origin,already_considered_nodes))
    return sizes


def full_check_cascade_size_recursive(repetitions=25,mu=0.2,beta=0.6,delay=2,weight_transfer=False):
    sizes = []
    for i in range(repetitions):
        g = pickle.load(open('graphs/new.pickle', 'rb'))
        sn = SecNet(g, mu, beta, reconnection_policy=ReconnectionPolicy.RANDOM, default_delay=delay, weight_transfer=weight_transfer)
        sn.run(100)
        sn.plot()
        sizes.append(check_cascade_size_recursive(sn.graph))
    
    return sizes
        
        