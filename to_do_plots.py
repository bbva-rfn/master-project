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
# definings how many itereations we want to do. 

# -------------------------------beta 0.4 -------------------------------------
niter = 100

density =  replicate_density(niter = niter,
                             beta = 0.4, 
                             default_delay =  4,
                             policy = ReconnectionPolicy.SOFT,
                             file_plot  = 'images/Replicate_density/beta_0.4/')
pct = pct_density(density,
                  niter = niter)

print(pct)


niter = 100

density =  replicate_density(niter = niter,
                             beta = 0.4, 
                             default_delay =  5,
                             policy = ReconnectionPolicy.SOFT,
                             file_plot  = 'images/Replicate_density/beta_0.4/')
pct = pct_density(density,
                  niter = niter)

print(pct)


# -------------------------------beta 0.5 -------------------------------------


niter = 100
density =  replicate_density(niter = niter,
                             beta = 0.5, 
                             default_delay =  2,
                             policy = ReconnectionPolicy.SOFT,
                             file_plot  = 'images/Replicate_density/beta_0.5/')
pct = pct_density(density,
                  niter = niter)

print(pct)


density =  replicate_density(niter = niter,
                             beta = 0.5, 
                             default_delay =  3,
                             policy = ReconnectionPolicy.SOFT,
                             file_plot  = 'images/Replicate_density/beta_0.5/')
pct = pct_density(density,
                  niter = niter)

print(pct)



density =  replicate_density(niter = niter,
                             beta = 0.5, 
                             default_delay =  4,
                             policy = ReconnectionPolicy.SOFT,
                             file_plot  = 'images/Replicate_density/beta_0.5/')
pct = pct_density(density,
                  niter = niter)

print(pct)


niter = 100

density =  replicate_density(niter = niter,
                             beta = 0.5, 
                             default_delay =  5,
                             policy = ReconnectionPolicy.SOFT,
                             file_plot  = 'images/Replicate_density/beta_0.5/')
pct = pct_density(density,
                  niter = niter)

print(pct)




'''
results_BA1 = pickle.load(open('BA/results/comparison_ratio2_SOFT[1, 3, 5, 7].pickle', 'rb'))
'''
