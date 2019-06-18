
from networkx import DiGraph
from SecNet import SecNet,ReconnectionPolicy
from joblib import Parallel,delayed
import numpy as np
import matplotlib.pyplot as plt
import pickle

def compare_density(graph:DiGraph,mu = 0.2,beta=0.6,max_iterations=150,repetitions=5,
                    policy = 'RANDOM', delays = [1,2,3,4],
                    filename = 'results/density/comparison'):
    
    if policy == 'NONE':
        recon_policy = ReconnectionPolicy.NONE
                       
    elif policy == 'RANDOM':
        recon_policy = ReconnectionPolicy.RANDOM 
                    
    elif policy == 'SOFT':
        recon_policy = ReconnectionPolicy.SOFT
                   
    elif policy == 'STRONG':
        recon_policy = ReconnectionPolicy.STRONG
        
    else:  
        print('policy not found.')
        return 0
    
    final_densities= []
    for delay in delays:
        densities = Parallel(n_jobs=-1)(delayed(run_density)(graph,mu, beta, recon_policy,delay, max_iterations) for _ in repetitions)
        #whatever
        densities = np.reshape(densities,(repetitions,max_iterations))
        final_densities.append(np.mean(densities,axis = 1))
    
    filename = filename + policy + str(delays)+ '.pickle'
    
    pickle.dump(final_densities, open(filename, 'wb'))
    
    return final_densities

def run_density(g:DiGraph,mu,beta,policy,delay,max_iterations):
    
    sn = SecNet(g,mu,beta,ReconnectionPolicy = policy,default_delay=delay)
    
    sn.run(max_iterations)
    
    return sn.defaulted_density
    
def plot_comparison_densities(densities:list,title='Density comparison',delays=[1,2,3,4],save=True,
                              filename='images/density/Density-comparison.png'):
    plt.figure()
    plt.title(title)
    for i in range(len(densities)):
        plt.plot(densities[i],label = 'Delay %s' %delays[i])
    plt.legend(loc='upper left')    
    plt.xlabel('Iteration')
    plt.ylabel('Density prob')
    
    if save:
        plt.savefig(filename)
        
    plt.show()