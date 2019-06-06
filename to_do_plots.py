import pickle
from SecNet import SecNet, ReconnectionPolicy
from plots_sis import beta_plot

g = pickle.load(open('graphs/new.pickle', 'rb'))

beta_plot(g,  mu = 0.2 , iterations = 75, policy = 'SOFT',default_delay= 2)
beta_plot(g,  mu = 0.2 , iterations = 75, policy = 'SOFT',default_delay= 4)
beta_plot(g,  mu = 0.2 , iterations = 75, policy = 'SOFT',default_delay= 8)

beta_plot(g,  mu = 0.2 , iterations = 75, policy = 'RANDOM',default_delay=2)
beta_plot(g,  mu = 0.2 , iterations = 75, policy = 'RANDOM',default_delay=4)
beta_plot(g,  mu = 0.2 , iterations = 75, policy = 'RANDOM',default_delay=8)

#
sn.plot()