#import networkx as nx
from cascades import plot_cascade_sizes,cascades_sizes_multiple
from sis_delay_comparison import compare_density,plot_comparison_densities
from sectorial_density_functions import sectorial_density,plot_sectorial_dataframe
import pickle
import time
#nx.draw(g,node_size=1)



start = time.time
g = pickle.load(open('BA/graph_ba.pickle', 'rb'))

sizes = cascades_sizes_multiple(g,mu=0.2,beta=0.4,delays=[2,3,4,5],policy='SOFT',repetitions=30,
                                filename='BA/results/cascade_size')


end = time.time

print(end-start)

plot_cascade_sizes(sizes,delays=[2,3,4,5],ylim = 10e-4,colors=['r','g','b','k'],
                   filename='BA/images/cascades_ratio2-SOFT.png')


start = time.time()

densities = compare_density(g,mu = 0.2,beta=0.6,repetitions=5,max_iterations=150,policy = 'SOFT',
                            delays=[1,2,3,4],filename='BA/results/comparison_ratio3_')
end = time.time()
print(end - start)

plot_comparison_densities(densities,delays=[1,2,3,4],
                          filename='BA/images/comparison_ratio3_SOFT.png')



start = time.time()

data = sectorial_density(g,repetitions=5,delay=4,mu = 0.2,beta=0.6,policy = 'SOFT',
                         filename='BA/results/Sectorial_',iterations=100)
end = time.time()
print(end - start)

plot_sectorial_dataframe(data,filename='BA/images/Sectorial_densitySOFT4.png')
