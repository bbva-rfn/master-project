import pickle

from joblib import Parallel, delayed

from SecNet import SecNet, ReconnectionPolicy
import time
import networkx as nx

start = time.time()

g = pickle.load(open('ER/graph_er.pickle', 'rb'))

print(g.number_of_nodes())
print(g.number_of_edges())
for node_id in g.nodes:
    node = g.nodes[node_id]
    print(node_id,node['sector'])
'''
def run():
    sn = SecNet(g, mu=0.2, beta=0.6, reconnection_policy=ReconnectionPolicy.SOFT)
    sn.run(30, verbose=False)
    

Parallel(n_jobs=-1, verbose=1)(delayed(run,)() for _ in range(4))

end = time.time()
print(end - start)

sn = SecNet(g, mu=0.2, beta=0.6,reconnection_policy=ReconnectionPolicy.SOFT,default_delay=2)
sn.run(70)
    
sn.plot()
# pickle.dump(sn, open('results/sto_random_weights.pickle', 'wb'))
'''