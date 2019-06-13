# -*- coding: utf-8 -*-
# adapting the code of cascades_old to the new general algorithm

from networkx import DiGraph
from SecNet import SecNet, ReconnectionPolicy
import matplotlib.pyplot as plt
import numpy as np
from risk_functions import set_initial_defaults
from joblib import Parallel, delayed


# as we store at which iteration they become infected it is trivial
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
        if neighbor['first_defaulted_at'] > node['first_defaulted_at'] and \
                neighbor['id'] not in already_considered_nodes:
            already_considered_nodes.append(neighbor['id'])
            s += check_infected_neighbours_recursive(graph, neighbor['id'], already_considered_nodes)
            s += 1

    return s


def check_cascade_size_recursive(graph: DiGraph):
    origins = cascade_origins(graph)
    sizes = []
    already_considered_nodes = []
    for origin in origins:
        already_considered_nodes.append(origin)
        sizes.append(check_infected_neighbours_recursive(graph, origin, already_considered_nodes))
    return sizes


def full_check_cascade_size_recursive(graph: DiGraph, repetitions=25, max_iterations=100,
                                      mu=0.2, beta=0.6, delay=2, weight_transfer=False,
                                      show=False, policy='RANDOM'):
    sizes = Parallel(n_jobs=-1)(delayed(run_simulation)(graph, mu, beta, policy, delay, weight_transfer, max_iterations, show) for _ in range(repetitions))
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
                                            delay=2, weight_transfer=False, iterations=100,
                                            show=True, policy='RANDOM'):
    sizes = []
    for i in range(repetitions):

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

        sn.run(iterations)
        if show:
            sn.plot()
        sizes.append(check_cascade_size_recursive(sn.graph))

    return sizes


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
    for i in range(max_size):
        add += i * probabilities[i]
    return add


def cascades_sizes_multiple(graph: DiGraph, repetitions=25, max_iterations=100,
                            mu=0.2, beta=0.6,
                            policy='RANDOM', delays=[2, 4, 6], weight_transfer=False,
                            filename='images/risk_cascades.png'):
    total_sizes = []
    for delay in delays:
        sizes = full_check_cascade_size_recursive(graph, repetitions=repetitions,
                                                  max_iterations=max_iterations, mu=mu,
                                                  beta=beta, policy=policy,
                                                  delay=delay, show=False)
        size = lists_to_list(sizes)
        total_sizes.append(size)

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

