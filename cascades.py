# -*- coding: utf-8 -*-
# adapting the code of cascades_old to the new general algorithm

from networkx import DiGraph
from SecNet import SecNet, ReconnectionPolicy
import matplotlib.pyplot as plt
import numpy as np
from risk_functions import set_initial_defaults
from joblib import Parallel, delayed
import pickle


# as we store at which iteration they become infected it is trivial
def cascade_origins(graph: DiGraph):
    origins = []
    for node_id in graph:
        node = graph.nodes[node_id]
        if node['first_defaulted_at'] == 0:
            origins.append(node_id)

    return origins

def check_infected_neighbours_recursive(graph: DiGraph, node_id, already_considered_nodes):
    s= 0
    node = graph.nodes[node_id]
    available = [item for item in graph.nodes if item not in already_considered_nodes]
    for node_i in available:
        node_new = graph.nodes[node_i]
        if node_new['first_defaulted_at'] > node['first_defaulted_at'] and \
                node_id in node_new['all_connected_nodes'] and \
                node_i not in already_considered_nodes:
            already_considered_nodes.append(node_new['id'])
            s += check_infected_neighbours_recursive(graph, node_new['id'], already_considered_nodes)
            s += 1

    return s

'''
Past check neighbours, for casade size we need to go the other way arround
def check_infected_neighbours_recursive(graph: DiGraph, node_id, already_considered_nodes):
    s = 0
    node = graph.nodes[node_id]
    neighbors = graph[node_id]
    neighbor_nodes = [graph.nodes[node_id] for node_id in list(neighbors)]
    for neighbor in neighbor_nodes:
        if neighbor['first_defaulted_at'] > node['first_defaulted_at'] and \
                neighbor['id'] not in already_considered_nodes:
            already_considered_nodes.append(neighbor['id'])
            s += check_infected_neighbours_recursive(graph, neighbor['id'], already_considered_nodes)
            s += 1

    return s
'''

def check_cascade_size_recursive(graph: DiGraph):
    origins = cascade_origins(graph)
    sizes = []
    already_considered_nodes = []
    for origin in origins:
        if(origin not in already_considered_nodes):
            already_considered_nodes.append(origin) 
            sizes.append(check_infected_neighbours_recursive(graph, origin, already_considered_nodes))
    return sizes


def full_check_cascade_size_recursive(graph: DiGraph, repetitions=25, max_iterations=100,
                                      mu=0.2, beta=0.6, delay=2, weight_transfer=False,
                                      show=False, policy='RANDOM'):
    sizes = Parallel(n_jobs=-1, verbose=10)(delayed(run_simulation)(graph, mu, beta, policy, delay, weight_transfer, max_iterations, show) for _ in range(repetitions))
    return sizes


def run_simulation(graph, mu, beta, policy, delay, weight_transfer, max_iterations, show):
    g = graph.copy()

    if policy == 'RANDOM':
        sn = SecNet(g, mu, beta, reconnection_policy=ReconnectionPolicy.RANDOM,
                    default_delay=delay, weight_transfer=weight_transfer)
    elif policy == 'SOFT':
        sn = SecNet(g, mu, beta, reconnection_policy=ReconnectionPolicy.SOFT,
                    default_delay=delay, weight_transfer=weight_transfer)
    else:
        print('Policy not understood')
        return 0

    sn.run(max_iterations,variation_coeff = 10e-5)
    if show:
        sn.plot()

    return check_cascade_size_recursive(sn.graph)


# modification for a general graph with option to change initial defaulted nodes
def full_check_cascade_size_setting_default(graph: DiGraph, node_id, repetitions=25, mu=0.2, beta=0.6,
                                            delay=2, weight_transfer=False, max_iterations=100,
                                            show=False, policy='RANDOM'):
    
    sizes = Parallel(n_jobs=-1)(delayed(run_simulation_set)(graph,node_id, mu, beta, policy,delay, weight_transfer, max_iterations, show) for _ in range(repetitions))
    return sizes


def run_simulation_set(graph,node_id, mu, beta, policy,
                     delay, weight_transfer, max_iterations, show):

    set_initial_defaults(graph, node_id)
    
    if policy == 'RANDOM':
        sn = SecNet(graph, mu, beta, reconnection_policy=ReconnectionPolicy.RANDOM,
                    default_delay=delay, weight_transfer=weight_transfer)
    elif policy == 'SOFT':
        sn = SecNet(graph, mu, beta, reconnection_policy=ReconnectionPolicy.SOFT,
                    default_delay=delay, weight_transfer=weight_transfer)
    else:
        print('Policy not understood')
        return 0

    sn.run(max_iterations,variation_coeff = 10e-5)
    if show:
        sn.plot()
        
    return check_cascade_size_recursive(sn.graph)




# Modification and better implementation of plotting cascade sizes

def lists_to_list(l):
    flat_list = [item for sublist in l for item in sublist]
    return flat_list


def cascade_size_plot(sizes, n, filename='images/cascade_size.png',
                      scatter=False):  # n is the number of nodes, if graph is not passed then we need it as argument
    if type(sizes[0]) == int and len(sizes) > 1:  # meaning there is only one list
        size = sizes

    elif type(sizes[0]) == list:
        size = lists_to_list(sizes)

    else:
        print('Error-Type not understood')

    max_size = max(size)
    prob = []
    for i in range(0, max_size + 1):
        p = 0
        for j in range(len(size)):
            if i == size[j]:
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
    if scatter:
        plt.scatter(np.arange(0, max_size + 1), inv_cum)
    else:
        plt.plot(np.arange(0, max_size + 1), inv_cum)

    plt.savefig(filename)
    plt.show()


def nice_cascade_plot_comparison(graph: DiGraph, repetitions=25, mu=0.2, beta=0.6, delays=[2, 4, 6], 
                                 colors=['r', 'b', 'g'], policy='RANDOM',
                                 filename='images/nice_cascade_plot_comparison.png'):
    plt.figure()
    plt.xlabel('Cascade size (Cs)')
    plt.ylabel('1-P(cs<Cs)')
    plt.xscale('log')
    plt.yscale('log')
    k = 0
    for delay in delays:
        sizes = full_check_cascade_size_recursive(graph, repetitions=repetitions, mu=mu, beta=beta,
                                                  policy=policy, delay=delay, show=False)
        size = lists_to_list(sizes)
        max_size = max(size)
        prob = []
        for i in range(max_size + 1):
            p = 0
            for j in range(len(size)):
                if i == size[j]:
                    p += 1
            p = p / len(size)
            prob.append(p)
        # now we have a list of probabilities and we need to do cumulative distribution
        inv_cum = 1 - np.cumsum(prob)

        lab = 'delay ' + str(delay)
        plt.plot(np.arange(0, max_size + 1), inv_cum, color=colors[k], label=lab)
        k += 1
    plt.legend()
    plt.tight_layout()
    plt.title('Inverse cumulative probability of Cascade size %s' % policy)
    plt.savefig(filename)
    plt.show()


def nice_cascade_plot_comparison_setting_defaults(graph: DiGraph, node_id, repetitions=25,
                                                  max_iterations=100, mu=0.2, beta=0.6,
                                                  delays=[2, 4, 6], 
                                                  colors=['r', 'b', 'g'], policy='RANDOM',
                                                  filename='images/nice_cascade_plot_change_default.png'):
    max_prob = []
    plt.figure()
    plt.xlabel('Cascade size (Cs)')
    plt.ylabel('1-P(cs<Cs)')
    plt.xscale('log')
    plt.yscale('log')
    k = 0
    for delay in delays:
        sizes = full_check_cascade_size_setting_default(graph, node_id, repetitions=repetitions,
                                                        iterations=max_iterations, mu=mu, beta=beta,
                                                        policy=policy,
                                                        delay=delay, show=False)
        size = lists_to_list(sizes)
        max_size = max(size)
        np.sqrt(np.sum(size))
        prob = []
        for i in range(max_size + 1):
            p = 0
            for j in range(len(size)):
                if i == size[j]:
                    p += 1
            p = p / len(size)
            prob.append(p)
        # now we have a list of probabilities and we need to do cumulative distribution
        inv_cum = 1 - np.cumsum(prob)
        max_prob.append([delay, most_probable(prob, max_size)])
        lab = 'delay ' + str(delay)
        plt.plot(np.arange(0, max_size + 1), inv_cum, color=colors[k], label=lab)
        k += 1
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()
    return max_prob


def risk_cascades(graph: DiGraph, node_id, repetitions=25, iterations=100, mu=0.2, beta=0.6,
                  policy='RANDOM', delays=[2, 4, 6], weight_transfer=False,
                  filename='images/risk_cascades.png'):
    risk = nice_cascade_plot_comparison_setting_defaults(graph, node_id, repetitions, iterations,
                                                         mu, beta, delays, policy=policy,
                                                         n=graph.number_of_nodes(), filename=filename)

    return risk


def most_probable(probabilities, max_size):
    add = 0
    for i in range(max_size+1):
        add += i * probabilities[i]
    return add


def cascades_sizes_multiple(graph: DiGraph, repetitions=25, max_iterations=100,
                            mu=0.2, beta=0.6,
                            policy='RANDOM', delays=[2, 4, 6], weight_transfer=False,
                            filename='results/cascades/'):
    total_sizes = []
    for delay in delays:
        sizes = full_check_cascade_size_recursive(graph, repetitions=repetitions,
                                                  max_iterations=max_iterations, mu=mu,
                                                  beta=beta, policy=policy,
                                                  delay=delay, show=False)
        size = lists_to_list(sizes)
        total_sizes.append(size)
    filename = filename + policy + str(delays) + '.pickle'
    pickle.dump(total_sizes, open(filename, 'wb'))
    return total_sizes


def plot_cascade_sizes(sizes: list, delays=[2, 4, 6], colors=['r', 'g', 'b'],
                       ylim = None ,filename='images/cascades/comparison_plot.png'):
    plt.figure()
    plt.xlabel('Cascade size (Cs)')
    plt.ylabel('1-P(cs<Cs)')
    plt.xscale('log')
    plt.yscale('log')
    if ylim != None:
        plt.ylim(ylim)
        
    k = 0
    max_prob = []
    for size in sizes:
        max_size = max(size)
        np.sqrt(np.sum(size))
        prob = []
        for i in range(max_size + 1):
            p = 0
            for j in range(len(size)):
                if i == size[j]:
                    p += 1
            p = p / len(size)
            prob.append(p)
        # now we have a list of probabilities and we need to do cumulative distribution
        inv_cum = 1 - np.cumsum(prob)
        max_prob.append([delays[k], most_probable(prob, max_size)])
        lab = 'delay ' + str(delays[k])
        plt.plot(np.arange(0, max_size + 1), inv_cum, color=colors[k], label=lab)
        k += 1
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()
    return max_prob

def cascades_setting_defaults(graph, node_id, repetitions, max_iterations,
                              mu, beta, delays, policy):
    
    total_sizes = []
    for delay in delays:
        sizes = full_check_cascade_size_setting_default(graph,node_id, repetitions=repetitions,
                                                  max_iterations=max_iterations, mu=mu,
                                                  beta=beta, policy=policy,
                                                  delay=delay, show=False)
        size = lists_to_list(sizes)
        total_sizes.append(size)

    return total_sizes

def assessment(sizes,delays):
    max_prob = np.zeros(len(delays))
    max_sizes = np.zeros(len(delays))
    k = 0
    for delay in delays:
        size = sizes[k]
        max_size = max(size)
        
        if max_size> max_sizes[k]:
            max_sizes[k]=max_size
            
        prob = []
        for i in range(max_size + 1):
            p = 0
            for j in range(len(size)):
                if i == size[j]:
                    p += 1
            p = p / len(size)
            prob.append(p)
        
        max_prob[k] = most_probable(prob, max_size)
        k += 1
        
    return max_prob,max_sizes


def risk_cascades_sectorial(graph: DiGraph, num_sectors, repetitions_per_node=15,
                            max_iterations=150, mu=0.2, beta=0.6, amount_per_sector=10,
                            policy='RANDOM', delays=[2, 4, 6]):
    
    risks = np.zeros(num_sectors*len(delays))
    maximums = np.zeros(num_sectors*len(delays))
    #doesnt matter what to pu tis just to apply the nodes by sector function
    sn = SecNet(graph, mu, beta, reconnection_policy=ReconnectionPolicy.RANDOM,
                    default_delay=2, weight_transfer=False)
    
    
    
    for sector in range(num_sectors):
        
        risk = np.zeros((amount_per_sector,len(delays)))
        maximum = np.zeros((amount_per_sector,len(delays)))
        eligible_nodes = sn.nodes_per_sector[sector]
        nodes = np.random.choice(eligible_nodes,size=amount_per_sector)
        r = 0
        for node_id in nodes:
            
            sizes = cascades_setting_defaults(graph, node_id, repetitions_per_node, max_iterations,
                                                 mu, beta, delays, policy=policy)
                                                         
            risk[r],maximum[r] = assessment(sizes,delays) 
            
            
            r+=1
        for i in range(len(delays)):
            risks[len(delays)*sector+i] = np.mean(risk[:,i])
            maximums[len(delays)*sector+i] = np.max(maximum[:,i])
            
        
            
    return risks,maximums

def sectorial_cascades_sizes(graph: DiGraph, num_sectors, repetitions_per_node=15,
                            max_iterations=150, mu=0.2, beta=0.6, nodes_per_sector=5,
                            policy='RANDOM', delay=[2]):
    
    sn = SecNet(graph, mu, beta, reconnection_policy=ReconnectionPolicy.RANDOM,
                    default_delay=2, weight_transfer=False)
    
    sector_sizes = []
    
    for sector in range(num_sectors):
        sizes = []
        eligible_nodes = sn.nodes_per_sector[sector]
        nodes = np.random.choice(eligible_nodes,size=nodes_per_sector)
        
        for node_id in nodes:
            size = cascades_setting_defaults(graph, node_id, repetitions_per_node, max_iterations,
                                                 mu, beta, delay, policy=policy)
            
            [sizes.append(siz) for siz in size]
            
        sector_sizes.append(sizes)
        
    
    return sector_sizes

def plot_sectorial_cascades(sizes,ylim = None,title='Title',
                            filename = 'images/cascades/sectorial_cascades.png'):
    
    plt.figure()
    plt.xlabel('Cascade size (Cs)')
    plt.ylabel('1-P(cs<Cs)')
    plt.xscale('log')
    plt.yscale('log')
    
    
         
    if ylim != None:
        plt.ylim(ylim)
        
    k = 0
    
    for size in sizes:
        max_size = max(size)
        
        prob = []
        for i in range(max_size + 1):
            p = 0
            for j in range(len(size)):
                if i == size[j]:
                    p += 1
            p = p / len(size)
            prob.append(p)
        # now we have a list of probabilities and we need to do cumulative distribution
        inv_cum = 1 - np.cumsum(prob)
        
        lab = 'Sector ' + str(k)
        plt.plot(np.arange(0, max_size + 1), inv_cum, label=lab)
        k += 1
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()
    
 
'''           
def run_and_save(graph: DiGraph, repetitions=5, max_iterations=100,
                            mu=0.2, beta=0.6,
                            policy=ReconnectionPolicy.RANDOM, delay=[4, 6],
                            weight_transfer=False,
                            filename='results/sn'):    
    
'''