import pickle
from SecNet import SecNet, ReconnectionPolicy

g = pickle.load(open('graphs/new.pickle', 'rb'))
sn = SecNet(g, mu=0.4, beta=0.8, stochastic=True, reconnection_policy=ReconnectionPolicy.NONE, default_delay=0)
sn.run(2)
# pickle.dump(sn, open('results/sto_no_reconnect.pickle', 'wb'))
