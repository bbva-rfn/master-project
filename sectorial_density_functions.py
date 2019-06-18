
from SecNet import SecNet,ReconnectionPolicy
import numpy as np
from joblib import delayed,Parallel
from networkx import DiGraph
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns; sns.set()
import pickle

def sectorial_density(graph:DiGraph,mu=0.2,beta=0.6,policy='RANDOM',delay = 2,
                      repetitions = 5, iterations = 150,num_sectors=17,
                      filename = 'results/density/Sectorial_density',on_dataframe = True):
    
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
    
    
    density_sectorial = Parallel(n_jobs=-1)(delayed(run_sectorial_d)(graph,mu, beta, recon_policy,
                                 delay, iterations,num_sectors) for _ in range(repetitions))
    
    if on_dataframe:
        density_dataframe = pd.DataFrame(columns=['Sector','Iteration','Density'])
        
        for i in range(repetitions):
            z = 0
            for sector in range(num_sectors):
                for j in range(iterations):
                    density_dataframe.loc[z] = [sector,j,density_sectorial[i][sector,j]]
                    z+=1
        filename = filename + policy + str(delay)+ '.pickle'
    
        density_dataframe.to_pickle(filename)
        
        return density_dataframe
    else:
        
        mean_density_sectorial = np.zeros((num_sectors,iterations))
        max_density_sectorial = np.zeros((num_sectors,iterations))
        min_density_sectorial = np.zeros((num_sectors,iterations))
        
        for sector in range(num_sectors):
            a = np.zeros(iterations)
            aux_max = 0
            aux_min = 1
            for i in range(repetitions):
                a += density_sectorial[i][sector,:]
                if density_sectorial[i][sector,-1] > aux_max:
                    aux_max = density_sectorial[i][sector,-1]
                    label_max = i
                if density_sectorial[i][sector,-1] < aux_min:
                    aux_min = density_sectorial[i][sector,-1] 
                    label_min = i
                    
            mean_density_sectorial[sector] = a/repetitions
            max_density_sectorial[sector] = density_sectorial[label_max][sector,:]
            min_density_sectorial[sector] = density_sectorial[label_min][sector,:]
        
        filename = filename + policy + str(delay)+ '.pickle'
        pickle.dump([mean_density_sectorial,max_density_sectorial,min_density_sectorial], open(filename, 'wb'))
        return mean_density_sectorial,max_density_sectorial,min_density_sectorial

    
def run_sectorial_d(graph,mu, beta, recon_policy,delay, iterations,num_sectors):
    
    sn = SecNet(graph, mu, beta,reconnection_policy = recon_policy, 
                default_delay = delay, weight_transfer = False)
    
    density_by_sector = np.zeros((num_sectors,iterations))
    
    for i in range(iterations):
        
        sn.run(1,verbose=False)
        
        for sector in range(num_sectors):
            nodes = sn.nodes_per_sector[sector]
            n = len(nodes)
            for node_id in nodes:
                node = sn.graph.nodes[node_id]
                density_by_sector[sector,i] += node['defaulted']
                
            density_by_sector[sector,i] = density_by_sector[sector,i] / n
            
    print("1 Done")
    return density_by_sector

def plot_sectorial_dataframe(data,filename='images/density/Sectorial_density_SOFT3.png',
                             title='Sectorial density'):
    plt.figure()
    plt.title(title)
    
    ax = sns.lineplot(x='Iteration', y='Density',hue = 'Sector', data=data)
    plt.savefig(filename)
    plt.show()
    
    
    
def plot_sectorial_density(mean_density_sectorial,max_density_sectorial,min_density_sectorial,
                           num_sectors = 17,save=True,title = 'Secotrial density',
                           filename= 'images/density/Sectorial_density_SOFT3.png'):
    
    plt.figure()
    plt.title(title)
    for i in range(num_sectors):
        plt.plot(mean_density_sectorial[i],label = 'Sector %s' %i)
    plt.legend(loc='upper left')    
    plt.xlabel('Iteration')
    plt.ylabel('Density prob')
    
    if save:
        plt.savefig(filename)
        
    plt.show()