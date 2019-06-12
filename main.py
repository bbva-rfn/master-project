import pickle

from SecNet import SecNet, ReconnectionPolicy

g = pickle.load(open('graphs/new.pickle', 'rb'))

sn = SecNet(g, mu=0.2, beta=0.6, reconnection_policy=ReconnectionPolicy.SOFT)
sn.run(200, 20, 0.015)
sn.plot()
# pickle.dump(sn, open('results/sto_random_weights.pickle', 'wb'))
