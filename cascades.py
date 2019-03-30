# -*- coding: utf-8 -*

import pickle
from networkx import DiGraph
from main import get_nodes_per_sector, iteration


def run_without_plot(g: DiGraph, num_iter=100):
    for i in range(0, num_iter):
        iteration(g)


def cascade_true_origins(graph: DiGraph):
    origins = []
    for node_id in graph:
        node = graph.nodes[node_id]
        if node['defaulted'] == 1:
            neighbors = graph[node['id']]
            if all([graph.nodes[node_id]['default'] != 1 for node_id in list(neighbors)]):
                origins.append(node_id)

    return origins


def cascade_fake_origins(graph: DiGraph):  # actually ends but better for size computation
    origins = list(range(graph.number_of_nodes()))  # this has to be a full list of all nodes id's or nodes or smthg
    for node_id in graph:
        node = graph.nodes[node_id]
        if node['defaulted'] != 1:
            origins.remove(node['id'])
        else:
            neighbors = graph[node['id']]
            for neighbor in neighbors.values():
                if neighbor['defaulted'] == 1:
                    origins.remove(neighbor['id'])
    return origins  # the only node id's remaining are the defaulted ones not pointed by any other defaulted node


def check_cascade_size(origins):
    sizes = []
    for origin in origins:
        sizes.append(check_infected_neighbours(origin))
    return sizes


def check_infected_neighbours(node, graph: DiGraph):
    s = 0
    neighbors = graph[node['id']]
    for neighbor in neighbors.values():
        if neighbor['defaulted'] == 1:
            s += check_infected_neighbours(neighbor)
            s += 1
    return s


# Parameters, modifiable
iterations = 100
beta = 0.5
mu = 0.4

# Load in graph
graph = pickle.load(open('graphs/new.pickle', 'rb'))

defaulted_density = []
nodes_per_sector = get_nodes_per_sector(graph)
run_without_plot(graph, iterations)

origins = cascade_fake_origins(graph)
size = check_cascade_size(origins)
print(size)
