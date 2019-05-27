import pickle

from SecNet import SecNet, ReconnectionPolicy

g = pickle.load(open('graphs/new.pickle', 'rb'))

sn = SecNet(g, mu=0.2, beta=0.6, reconnection_policy=ReconnectionPolicy.RANDOM, default_delay=0)
sn.run(100)
pickle.dump(sn, open('results/sto_random.pickle', 'wb'))
