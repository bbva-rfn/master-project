
from sectorial_density_functions import sectorial_density,plot_sectorial_dataframe
import pickle
import time

g = pickle.load(open('graphs/new.pickle', 'rb'))
start = time.time()

data = sectorial_density(g,repetitions=5,delay=4,mu = 0.2,beta=0.6,policy = 'SOFT',
                         filename='results/density/Sectorial_',iterations=100)
end = time.time()
print(end - start)

plot_sectorial_dataframe(data,filename='images/density/Sectorial_densitySOFT4.png')


'''
data = pickle.load(open('results/density/Sectorial_dens_provaSOFT3.pickle', 'rb'))
print(data)
plot_sectorial_dataframe(data)
'''