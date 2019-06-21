#import networkx as nx
from cascades import plot_cascade_sizes,cascades_sizes_multiple
from sis_delay_comparison import compare_density,plot_comparison_densities
from sectorial_density_functions import sectorial_density,plot_sectorial_dataframe
import pickle
import time




start = time.time()
g = pickle.load(open('ER/graph_er.pickle', 'rb'))

sizes = cascades_sizes_multiple(g,mu=0.2,beta=0.4,delays=[2,3,4,5],policy='SOFT',repetitions=30,
                                filename='ER/results/cascades_ratio2')

#sizes = pickle.load(open('BA/results/cascade_sizeSOFT[2, 3, 4, 5].pickle','rb'))
end = time.time()

print(end-start)

plot_cascade_sizes(sizes,delays=[2,3,4,5],ylim = 10e-4,colors=['r','g','b','k'],
                   filename='ER/images/cascades_ratio2-SOFT.png')


start = time.time()

densities = compare_density(g,mu = 0.2,beta=0.6,repetitions=8,max_iterations=150,policy = 'SOFT',
                            delays=[1,2,4,6],filename='ER/results/comparison_ratio3_')
end = time.time()
print(end - start)

plot_comparison_densities(densities,delays=[1,2,4,6],
                          filename='ER/images/comparison_ratio3_SOFT.png')


'''
start = time.time()

data = sectorial_density(g,repetitions=8,delay=4,mu = 0.2,beta=0.6,policy = 'SOFT',
                         filename='BA/results/Sectorial_',iterations=100,num_sectors=5)
end = time.time()
print(end - start)

plot_sectorial_dataframe(data,filename='BA/images/Sectorial_densitySOFT4.png')
'''