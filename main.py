import pickle

from joblib import Parallel, delayed

from SecNet import SecNet, ReconnectionPolicy
import time

start = time.time()

g = pickle.load(open('graphs/new.pickle', 'rb'))


def run():
    sn = SecNet(g, mu=0.2, beta=0.6, reconnection_policy=ReconnectionPolicy.SOFT)
    sn.run(30, verbose=False)


Parallel(n_jobs=-1, verbose=1)(delayed(run,)() for _ in range(4))

end = time.time()
print(end - start)
# sn.plot()
# pickle.dump(sn, open('results/sto_random_weights.pickle', 'wb'))
