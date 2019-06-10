# -*- coding: utf-8 -*-
#adapting the code of cascades_old to the new general algorithm

from networkx import DiGraph
import pickle
from SecNet import SecNet, ReconnectionPolicy
import matplotlib.pyplot as plt
import numpy as np

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
        

#Modification and better implementation of ploting cascade sizes
    
def lists_to_list(l):
    flat_list = [item for sublist in l for item in sublist]
    return flat_list


def cascade_size_plot(sizes, n,filename='images/cascade_size.png'):  # n is the number of nodes, if graph is not passed then we need it as argument
    if type(sizes[0]) == int and len(sizes) > 1:  # meaning there is only one list
        size = sizes
        
    elif type(sizes[0])==list:
        size = lists_to_list(sizes)
            
    else:
        print('Error-Type not understood') 
        
    max_size = max(size)
    prob = []
    for i in range(0, max_size + 1):
        p = 0
        for j in range(len(size)):
            if (i == size[j]):
                p += 1
        p = p / n
        prob.append(p)
    # now we have a list of probabilities and we need to do cumulative distribution
    inv_cum = 1 - np.cumsum(prob)

    plt.figure()
    plt.xlabel('cs')
    plt.ylabel('1-P(cs<Cs)')
    plt.xscale('log')
    plt.yscale('log')
    plt.plot(np.arange(0, max_size + 1), inv_cum)
    plt.savefig(filename)
    plt.show()
        