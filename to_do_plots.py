import pickle
import numpy as np
from SecNet import SecNet, ReconnectionPolicy
from plots_sis import beta_plot, density_plot
from replicate_density import replicate_density, pct_density

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


## niterations to see how consistent it is and the percentage of 0 and equilibirums:


density =  replicate_density(niter = 100,
                             beta = 0.4, 
                             default_delay =  4,
                             policy = ReconnectionPolicy.SOFT,
                             file_plot  = 'images/Replicate_density/beta_0.4/')
pct = pct_density(density,
                  niter = 2)

print(pct)
