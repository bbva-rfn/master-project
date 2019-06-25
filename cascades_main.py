from cascades import plot_cascade_sizes,cascades_sizes_multiple
import pickle
import time

start = time.time()
g = pickle.load(open('BA/graph_ba.pickle', 'rb'))

sizes = cascades_sizes_multiple(g,mu=0.2,beta=0.4,delays=[6,7,8],policy='SOFT',repetitions=20,
                                filename='BA/results/cascades/')


end = time.time()

print(end-start)

print(sizes)

plot_cascade_sizes(sizes,delays=[3,4,5],ylim = 10e-4,colors=['r','g','b','k'],
                   filename='BA/images/cascades/compa3_SOFT.png')
