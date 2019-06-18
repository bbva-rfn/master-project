from sis_delay_comparison import compare_density,plot_comparison_densities
import pickle
import time

g = pickle.load(open('graphs/new.pickle', 'rb'))
start = time.time()

densities = compare_density(g,mu = 0.2,beta=0.6,repetitions=5,max_iterations=100,
                            delays=[1,2],filename='results/density/comparison_prova')
end = time.time()
print(end - start)

plot_comparison_densities(densities,delays=[1,2])
