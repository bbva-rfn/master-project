from cascades import plot_cascade_sizes,cascades_sizes_multiple
import pickle
import time

start = time.time()
g = pickle.load(open('ER/graph_er.pickle', 'rb'))



sizes = cascades_sizes_multiple(g,mu=0.2,beta=0.6,delays=[1,6],policy='SOFT',repetitions=30,
                                filename='ER/results/cascades/')

end = time.time()

print(end-start)

print(sizes)

res = plot_cascade_sizes(sizes,delays=[1,6],ylim = 10e-4,colors=['r','g','b','k'],
                   filename='ER/images/cascades/compa4_SOFT3.png')

print(res)
