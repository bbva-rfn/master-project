from cascades import plot_cascade_sizes,cascades_sizes_multiple
import pickle
import time

start = time.time()
g = pickle.load(open('ER/graph_er.pickle', 'rb'))

sizes = cascades_sizes_multiple(g,mu=0.2,beta=0.6,delays=[2,3,4,5],policy='RANDOM',repetitions=30,
                                filename='ER/results/cascades/ratio3_')


end = time.time()

print(end-start)

print(sizes)

plot_cascade_sizes(sizes,delays=[2,3,4,5],ylim = 10e-4,colors=['r','g','b','k'],
                   filename='ER/images/cascades/compa2_RANDOM3.png')
