import pickle
from plots_sis import plot_sectorial_multi_beta
from sis_delay_comparison import plot_comparison_densities
import numpy as np
from cascades import plot_cascade_sizes

'''
probs = pickle.load(open('BBVA/results/density_sectorialSOFT2.pickle', 'rb'))

names = {'0':'Stark' , '1':'Bolton', '2':'Umber','3':'Manderly','4':'Hornwood','5':'Glover',
         '6':'Tallhart','7':'Dustin','8':'Reed','9':'Flynt','10':'Mormont','11':'Karstark',
         '12':'Cassel','13':'Poole','14': 'Frey'  ,'15': 'Tully','16':'Mallister','17':'Snow'}

betas = np.arange(0,1,0.1)
plot_sectorial_multi_beta(probs,names,betas,filename='BBVA/images/sectorial_density1.png')

densities = pickle.load(open('BBVA/results/comparison_ratio2_SOFT[1, 2, 3, 4, 5, 6, 7].pickle', 'rb'))

plot_comparison_densities(densities,delays=[1,2,3,4,5,6,7],
                          filename='BBVA/images/comparison_ratio2_SOFT.png')



'''
sizes1 = pickle.load(open('ER/results/cascades/SOFT[1, 6].pickle', 'rb'))
sizes2 = pickle.load(open('ER/results/cascades/ratio3_SOFT[2, 3, 4, 5].pickle', 'rb'))


[sizes1.append(siz) for siz in sizes2]

res = plot_cascade_sizes(sizes1,delays=[1,6,2,3,4,5],title='0.6',
                   filename='ER/images/cascades/full2_ratio3.png')

print(res)
