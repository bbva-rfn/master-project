import numpy as np
import pickle

import networkx
from networkx import set_node_attributes

from SecNet import SecNet, ReconnectionPolicy

# g = pickle.load(open('graphs/new.pickle', 'rb'))
from SecNetSimple import SecNetSimple

g = networkx.read_weighted_edgelist('anim&risk/celegans_edges.txt')
set_node_attributes(g, 0, name='defaulted')

for node_id in g:
    g.nodes[node_id]['id'] = node_id

for i in np.random.randint(0, g.number_of_nodes(), 10):
    g.nodes[str(i)]['defaulted'] = 1

sn = SecNetSimple(g, mu=0.2, beta=0.4)
sn.run(75)
pickle.dump(sn, open('results/ramon_sto_no_reconnect.pickle', 'wb'))
