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
                      policy = ReconnectionPolicy.SOFT,
                      file_plot  = 'images/Replicate_density/beta_0.4' ):
    dens = []
    densities = []
    fig = figure()
    plot = fig.add_subplot(111)
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
        fig.suptitle(' Simulations function with n = %s'%niter )
        plt.xlabel('Iteratuinons')
        plt.ylabel('Density ')
    file  =  file_plot + str(policy) + str(beta)+ str(default_delay)+'.png'
    fig.savefig(file)
    show()
        
    return (dens)



def pct_density(dens,
                niter = 100):
    count = 0
    for i in range(niter):
        if (np.array(dens[i]) > 0.1):
            count = count + 1       
    percnt = (count/niter)
    return (percnt)
