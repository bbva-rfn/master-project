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
sn = SecNet(g, mu = 0.2, beta = 0.6, 
                                reconnection_policy = ReconnectionPolicy.RANDOM, 
                                default_delay = 2  , weight_transfer = False)
sn.run(150,variation_coeff = 10e-5)
print(sn.defaulted_density)
print(np.mean(sn.defaulted_density[-10:]))
sn.plot()