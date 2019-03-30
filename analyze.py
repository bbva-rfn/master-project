import pickle
import matplotlib.pyplot as plt
import networkx
from SecNet import SecNet
from cascades import cascade_fake_origins

sn = pickle.load(open('results/test.pickle', 'rb'))
graph = sn.graph

print(cascade_fake_origins(graph))

# plt.figure(figsize=(12, 12))
# networkx.draw_spectral(graph, with_labels=False, node_size=10)
# plt.show()
