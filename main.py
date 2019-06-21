import pickle

from joblib import Parallel, delayed
import numpy as np
from SecNet import SecNet, ReconnectionPolicy
import time
import networkx as nx
import matplotlib.pyplot as plt
from sectorial_density_functions import density_with_sigma,plot_density_sigma

g = pickle.load(open('BA/graph_ba.pickle', 'rb'))

    
def pct_density(dens,
                niter = 100):
    d_aux = dens[dens['Iteration']== 140]['Density'].values
    count = 0
    for i in range(niter):
        if (np.array(d_aux)[i] > 0.4):
            count = count + 1       
    percnt = (count/niter)
    return (percnt)

def pct_density_inv(dens,
                niter = 100):
    d_aux = dens[dens['Iteration']== 140]['Density'].values
    count = 0
    for i in range(niter):
        if (np.array(d_aux)[i] <  0.05):
            count = count + 1       
    percnt = (count/niter)
    return (percnt)


name_or = 'BA/results/density_2_SOFT'
for delay in [7,8,9,10]:
    name = name_or+str(delay)+'.pickle'
    name2 = 'BA/images/replicate/density_2_SOFT'+str(delay)+'.png'
    densities = density_with_sigma(g,beta=0.4,delay = delay,repetitions=100,filename=name)
    plot_density_sigma(densities,filename=name2)
    pct1 = pct_density(densities,
                niter = 100 )
    print(pct1)
    pct2 = pct_density_inv(densities,
                niter = 100 )
    
    print(pct2)




'''
start = time.time()
g = pickle.load(open('BBVA/bbva.pickle', 'rb'))
sn = SecNet(g, mu=0.2, beta=0.6, reconnection_policy=ReconnectionPolicy.SOFT, default_delay=3)
sn.run(150)

end = time.time()
print(end - start)
'''
'''
start = time.time()

g = pickle.load(open('BA/graph_ba.pickle', 'rb'))

sn = SecNet(g, mu=0, beta=0.6, reconnection_policy=ReconnectionPolicy.SOFT)
sn.run(150, verbose=False)

density_sto = sn.defaulted_density

sn = SecNet(g, mu=0, beta=0.6, reconnection_policy=ReconnectionPolicy.SOFT,stochastic=False)
sn.run(150, verbose=False)

density_con = sn.defaulted_density

plt.figure()
plt.title('mu = 0')
plt.plot(density_sto,label='Stochastic',color='b')
plt.plot(density_con,label='Continuous', color = 'r')
plt.legend()
plt.savefig('images/density/mu0sto-compa.png')
plt.show()

plt.figure()
plt.plot(density_sto,color='b')
plt.savefig('images/density/stomu0.png')
plt.show()
#densities = density_with_sigma(g)
#plot_density_sigma(densities)
'''
'''
g = pickle.load(open('ER/graph_er.pickle', 'rb'))

print(g.number_of_nodes())
print(g.number_of_edges())
for node_id in g.nodes:
    node = g.nodes[node_id]
    print(node_id,node['sector'])

def run():
    sn = SecNet(g, mu=0.2, beta=0.6, reconnection_policy=ReconnectionPolicy.SOFT)
    sn.run(30, verbose=False)
    

Parallel(n_jobs=-1, verbose=1)(delayed(run,)() for _ in range(4))

end = time.time()
print(end - start)


'''