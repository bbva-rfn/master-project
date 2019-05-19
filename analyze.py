import pickle
import matplotlib.pyplot as plt
import networkx
from SecNet import SecNet
from cascades import cascade_fake_origins,check_cascade_size_recursive
from plots_sis import cascade_size_plot

sn = pickle.load(open('results/nonsto_random_wait.pickle', 'rb'))
sn.plot()

# origins = cascade_fake_origins(graph)
# cascade_size = check_cascade_size_recursive(graph, origins)
#cascade_size = check_cascade_size(graph, origins)
# print(cascade_size)

# n = graph.number_of_nodes()

# cascade_size_plot(cascade_size,n)

# plt.figure(figsize=(12, 12))
# networkx.draw_spectral(graph, with_labels=False, node_size=10)

