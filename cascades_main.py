from cascades import plot_cascade_sizes,cascades_sizes_multiple
import pickle
import time

start = time.time()
g = pickle.load(open('BBVA/bbva.pickle', 'rb'))

sizes = cascades_sizes_multiple(g,mu=0.2,beta=0.4,delays=[5,6],policy='SOFT',repetitions=50,
				filename='BBVA/results/cascades_')

end = time.time()

print(end-start)

#print(sizes)

#res = plot_cascade_sizes(sizes,delays=[1,9],ylim = 10e-4,
#                         filename='BA/images/cascades/compa6_SOFT3.png')

#print(res)
