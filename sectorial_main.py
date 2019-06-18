
from sectorial_density_functions import sectorial_density,plot_sectorial_dataframe
import pickle
import time

g = pickle.load(open('graphs/new.pickle', 'rb'))
start = time.time()

data = sectorial_density(g,repetitions=5,delay=3,mu = 0.2,beta=0.6,policy = 'SOFT',
                         filename='results/density/Sectorial_dens_prova',iterations=100)
end = time.time()
print(end - start)

plot_sectorial_dataframe(data)

#fmri = sns.load_dataset("fmri")
#ax = sns.lineplot(x="timepoint", y="signal", data=fmri)

'''
data = pickle.load(open('results/density/Sectorial_dens_provaSOFT3.pickle', 'rb'))
print(data)
plot_sectorial_dataframe(data)
'''