import pickle
import numpy as np
from SecNet import SecNet, ReconnectionPolicy
from plots_sis import beta_plot, density_plot

g = pickle.load(open('graphs/new.pickle', 'rb'))

#beta_plot(g,  mu = 0.2 , iterations = 75, policy = 'SOFT',default_delay= 2)
#beta_plot(g,  mu = 0.2 , iterations = 75, policy = 'SOFT',default_delay= 4)
#beta_plot(g,  mu = 0.2 , iterations = 75, policy = 'SOFT',default_delay= 8)
#beta_plot(g,  mu = 0.2 , iterations = 75, policy = 'RANDOM',default_delay=2)
#beta_plot(g,  mu = 0.2 , iterations = 75, policy = 'RANDOM',default_delay=4)
#beta_plot(g,  mu = 0.2 , iterations = 75, policy = 'RANDOM',default_delay=8)
'''
density_plot(g, 
             mu = 0.2, 
             beta = 0.6,
             iterations = 200)
         
'''
def replicate_density (niter = 100, 
                       beta = 0.6):
    dens = []
    for i in range (niter):
        sn = SecNet(g, mu = 0.2, 
                    beta = beta, 
                    reconnection_policy = ReconnectionPolicy.SOFT, 
                    default_delay = 2  , 
                    weight_transfer = False)
        sn.run(400,variation_coeff = 10e-5)
        sn.plot()
        dens.append( sn.defaulted_density[- 1] )
        print(i)
        return (dens)

replicate_density(niter 100, beta = 0.5 )

def pct_density(dens):
    count = 0
    for i in range(100):
        if (np.array(dens[i]) > 0.1):
            count = count + 1       
    print(count/100)


replicate_density(dens)