import pickle
from SecNet import SecNet, ReconnectionPolicy

g = pickle.load(open('graphs/new.pickle', 'rb'))
sn = SecNet(g, mu=0.4, beta=0.5, stochastic=False, reconnection_policy=ReconnectionPolicy.RANDOM, default_delay=20)
sn.run(100)
pickle.dump(sn, open('results/nonsto_random_wait.pickle', 'wb'))
