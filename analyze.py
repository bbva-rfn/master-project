import pickle
import matplotlib.pyplot as plt
import networkx
from SecNet import SecNet
from cascades import cascade_fake_origins, check_cascade_size

sn = pickle.load(open('results/test.pickle', 'rb'))
graph = sn.graph


origins = cascade_fake_origins(graph)
cascade_size = check_cascade_size(graph, origins)

# plt.figure(figsize=(12, 12))
# networkx.draw_spectral(graph, with_labels=False, node_size=10)
# plt.show()
