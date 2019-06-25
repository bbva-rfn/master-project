from cascades import plot_cascade_sizes,cascades_sizes_multiple
import pickle
import time

start = time.time()
g = pickle.load(open('BA/graph_ba.pickle', 'rb'))



sizes = cascades_sizes_multiple(g,mu=0.2,beta=0.6,delays=[1,6],policy='SOFT',repetitions=30,
                                filename='BA/results/cascades/')

end = time.time()

print(end-start)

print(sizes)

res = plot_cascade_sizes(sizes,delays=[1,6],ylim = 10e-4,
                         filename='BA/images/cascades/compa4_SOFT3.png')

print(res)