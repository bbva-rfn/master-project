# -*- coding: utf-8 -*

from networkx import DiGraph


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
            neighbor_nodes = [graph.nodes[node_id] for node_id in list(neighbors)]
            for neighbor in neighbor_nodes:
                if neighbor['defaulted'] and neighbor['id'] in origins:
                    origins.remove(neighbor['id'])
    return origins  # the only node id's remaining are the defaulted ones not pointed by any other defaulted node

def check_cascade_size_recursive(graph: DiGraph, origins):
    sizes = []
    for origin in origins:
        sizes.append(check_infected_neighbours_recursive(graph, origin))
    return sizes


def check_infected_neighbours_recursive(graph: DiGraph, node_id, already_considerer_nodes = []):
    s = 0
    already_considerer_nodes.append(node_id)
    neighbors = graph[node_id]
    neighbor_nodes = [graph.nodes[node_id] for node_id in list(neighbors)]
    for neighbor in neighbor_nodes:
        if neighbor['defaulted'] and neighbor['id'] not in already_considerer_nodes:
            s += check_infected_neighbours_recursive(graph, neighbor['id'])
            s += 1
            already_considerer_nodes.append(neighbor['id'])
    return s


#recursive functions do not work well in python so we need other options
#not sure which other options exists
def check_cascade_size(graph: DiGraph, origins):
    sizes = []
    for origin in origins:
        sizes.append(check_infected_neighbours(graph, origin))
    return sizes

def check_infected_neighbours(graph:DiGraph,node_id):
    s = 0
    neighbors = graph[node_id]
    new_origins = []
    neighbor_nodes = [graph.nodes[node_id] for node_id in list(neighbors)]
    for neighbor in neighbor_nodes:
        if neighbor['defaulted'] and neighbor['id'] != node_id:
            new_origins.append(neighbor['id']) 
            s += 1
    return s,new_origins