import pickle
import numpy as np
from SecNet import SecNet, ReconnectionPolicy
from plots_sis import beta_plot, density_plot
from matplotlib.pyplot import figure, show
import matplotlib.pyplot as plt

g = pickle.load(open('graphs/new.pickle', 'rb'))


def replicate_density(niter = 100, 
                      beta = 0.6,
                      default_delay = 2,
                      policy = ReconnectionPolicy.SOFT):
    dens = []
    densities = []
    fig = figure()
    plot = fig.add_subplot(111)
    file  = 'images/Replicate_density/beta_0.4/replicate_density.png' 
    for i in range(niter):
        sn = SecNet(g, mu = 0.2, 
                    beta = beta, 
                    reconnection_policy = policy, 
                    default_delay = default_delay, 
                    weight_transfer = False)
        sn.run(400,variation_coeff = 10e-5)
        plot.plot(sn.defaulted_density)
        dens.append(sn.defaulted_density[- 1])
        sn.defaulted_density
        fig.suptitle('%s' %niter + '\t number of densities simulations with policiy %s' %policy + 
         '\t and for beta %s' %beta )
    fig.savefig(file)
    show()
        
    return (dens)

density =  replicate_density(niter = 2,
                             beta = 0.4, 
                             default_delay =  2,
                             policy = ReconnectionPolicy.SOFT)

def pct_density(dens,
                niter = 2):
    count = 0
    for i in range(niter):
        if (np.array(dens[i]) > 0.1):
            count = count + 1       
    percnt = (count/niter)
    return (percnt)

pct = pct_density(density, niter = 2)
print(pct)
