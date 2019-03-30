# -*- coding: utf-8 -*-

import pickle

import numpy as np
import matplotlib.pyplot as plt
from main import SecNet

# Load in graph + parameters
def construct_probs_by_sector(density_probs):
    probs = []
    l = len(density_probs[0])
    for i in range (0,l):
        p =[]
        for prob in density_probs:
            p.append(prob[i])
        probs.append(p)
    return probs
        
mu = 0.4
betas = np.arange(0,1,0.1)
iterations = 50

density_probs = []
g = pickle.load(open('graphs/new.pickle', 'rb'))

for beta in betas:
    sn = SecNet(g, mu, beta)
    sn.run(iterations)
    #sn.graph to access the copied graph
    prob_by_sector = np.zeros(17)

    for sector in range(0,17):
        nodes = sn.nodes_per_sector[sector]
        n = len(nodes)
        for node_id in nodes:
            node = g.nodes[node_id]
            prob_by_sector[sector] += node['defaulted']
        prob_by_sector[sector] = prob_by_sector[sector]/n
    
    density_probs.append(prob_by_sector)


probs_by_sector = construct_probs_by_sector(density_probs)
print(probs_by_sector)
plt.figure() 
for prob in probs_by_sector:
    plt.plot(betas,prob)
plt.xlabel('betas')
plt.ylabel('density prob')
plt.show()

