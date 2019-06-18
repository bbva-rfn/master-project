from sis_delay_comparison import compare_density,plot_comparison_densities
import pickle
import time

g = pickle.load(open('graphs/new.pickle', 'rb'))
start = time.time()

densities = compare_density(g,mu = 0.2,beta=0.6,repetitions=5,max_iterations=150,policy = 'SOFT',
                            delays=[1,2,3,4],filename='results/density/comparison_ratio3_')
end = time.time()
print(end - start)

plot_comparison_densities(densities,delays=[1,2,3,4],filename='images/density/comparison_ratio3_SOFT.png')

'''
densities = pickle.load(open('results/density/comparison_provaSOFT[1, 2, 3, 4].pickle', 'rb'))
plot_comparison_densities(densities,delays=[1,2,3,4],
                          filename='images/density/comparison_provaSOFT.png')
'''