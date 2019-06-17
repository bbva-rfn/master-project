# -*- coding: utf-8 -*-

import pickle

import numpy as np
import matplotlib.pyplot as plt
from SecNet import SecNet, ReconnectionPolicy
from networkx import DiGraph


# Load in graph + parameters
def construct_probs_by_sector(density_probs):
    probs = []
    l = len(density_probs[0])
    for i in range(0, l):
        p = []
        for prob in density_probs:
            p.append(prob[i])
        probs.append(p)
    return probs


def beta_plot(g: DiGraph, 
              mu = 0.1, 
              iterations = 75, 
              file_plot=  'images/prob_by_sector',
              policy = 'SOFT',
              default_delay = 4):

    betas = np.arange(0, 1, 0.02)

    density_probs = []

    for beta in betas:
        if policy == 'NONE':
            sn = SecNet(g, mu, beta, 
                        reconnection_policy = ReconnectionPolicy.NONE, 
                        default_delay = default_delay, weight_transfer = False)
        elif policy == 'RANDOM':
            sn = SecNet(g, mu, beta, 
                        reconnection_policy = ReconnectionPolicy.RANDOM, 
                        default_delay = default_delay, weight_transfer = False)
        elif policy == 'SOFT':
            sn = SecNet(g, mu, beta, 
                        reconnection_policy = ReconnectionPolicy.SOFT, 
                        default_delay = default_delay, weight_transfer = False)
        elif policy == 'STRONG':
            sn = SecNet(g, mu, beta, 
                        reconnection_policy = ReconnectionPolicy.STRONG, 
                        default_delay = default_delay, weight_transfer = False)
        else:  return('policy not found.')
            
        sn.run(iterations)
        # sn.graph to access the copied graph
        prob_by_sector = np.zeros(17)

        for sector in range(0, 17):
            nodes = sn.nodes_per_sector[sector]
            n = len(nodes)
            for node_id in nodes:
                node = sn.graph.nodes[node_id]
                prob_by_sector[sector] += node['defaulted']
            prob_by_sector[sector] = prob_by_sector[sector] / n

        density_probs.append(prob_by_sector)

    print(density_probs)

    probs_by_sector = construct_probs_by_sector(density_probs)
    print(probs_by_sector)
    plt.figure()
    for prob in probs_by_sector:
        plt.plot(betas, prob)
        plt.legend(loc='upper left')   
    plt.title('Random sample with %s reconnection policy' %policy)
    plt.legend(loc='upper left')    
    plt.xlabel('betas')
    plt.ylabel('density prob')
    file  =  file_plot + policy + str(default_delay)+'.png'
    plt.savefig(file)
    plt.show()


def cascade_size_plot(sizes, n):  # n is the number of nodes, if graph is not passed then we need it as argument
    if type(sizes[0]) == int and len(sizes) > 1:  # meaning there is only one list
        max_sizes = max(sizes)
        prob = []
        for i in range(0, max_sizes + 1):
            p = 0
            for j in range(0, len(sizes)):
                if (i == sizes[j]):
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
        plt.plot(np.arange(0, max_sizes + 1), inv_cum)
        plt.savefig('images/cascade_size.png')
        plt.show()
    else:
        print('Not implemented yet for larger sizes')



def density_plot(g:DiGraph, 
                  mu = 0.4, 
                  beta = 0.6,
                  iterations = 200,
                  file_plot= 'images/density/density_by_policy'):
    
        for policy in ['SOFT','RANDOM']:
            for default_delay in [2,4,6,8]:
                if policy == 'NONE':
                    sn = SecNet(g, mu = mu, beta =beta, 
                                reconnection_policy = ReconnectionPolicy.NONE, 
                                default_delay= 0 , weight_transfer = False)
                elif policy == 'RANDOM':
                    sn = SecNet(g, mu = mu, beta = beta, 
                                reconnection_policy = ReconnectionPolicy.RANDOM, 
                                default_delay = default_delay  , weight_transfer = False)
                elif policy == 'SOFT':
                    sn = SecNet(g, mu = mu, beta = beta, 
                                reconnection_policy = ReconnectionPolicy.SOFT, 
                                default_delay = default_delay  , weight_transfer = False)
                elif policy == 'STRONG':
                    sn = SecNet(g, mu = mu, beta = beta, 
                                reconnection_policy = ReconnectionPolicy.STRONG, 
                                default_delay = default_delay , weight_transfer = False)
                file  =  file_plot + policy + str(default_delay)+'.png'
                sn.run(iterations, variation_coeff = 10e-5)    
                sn.plot('Defaulted companies for %s' %policy,
                        save = True ,
                        file_name =  file)
                
                        
'''                    
def sectorial_density_plot(g:DiGraph,mu=0.2,beta=0.6,max_iterations=200,policy = 'RANDOM',
                           delay = 2, number_sectors = 5,title = 'Title',save = True,
                           filename='images/density/sectorial_density.png'):
    if policy == 'NONE':
        sn = SecNet(g, mu = mu, beta =beta, 
                    reconnection_policy = ReconnectionPolicy.NONE, 
                    default_delay= 0 , weight_transfer = False)
    elif policy == 'RANDOM':
        sn = SecNet(g, mu = mu, beta = beta, 
                    reconnection_policy = ReconnectionPolicy.RANDOM, 
                    default_delay = delay  , weight_transfer = False)
    elif policy == 'SOFT':
        sn = SecNet(g, mu = mu, beta = beta, 
                    reconnection_policy = ReconnectionPolicy.SOFT, 
                    default_delay = delay  , weight_transfer = False)
    else:
        print('Error in policy selection')
        return 0
    
    sn.run(max_iterations,variation_coeff=10e-5)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for sector in range(number_sectors):
        lab = 'Sector' + str(sector)
        ax.plot(self.defaulted_density,label = lab)
        
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Density')
    ax.set_title(title)
    fig.tight_layout()
    if save:
        fig.savefig(filename)
    plt.show()
'''
    