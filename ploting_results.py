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

densities = pickle.load(open('BBVA/results/comparison_ratio3_SOFT[2, 3].pickle', 'rb'))

plot_comparison_densities(densities,delays=[2,3],
                          filename='BBVA/images/comparison_ratio3_SOFT.png')

'''


sizes1 = pickle.load(open('BA/results/cascades/SOFT[1, 6].pickle', 'rb'))
#sizes2 = pickle.load(open('BA/results/cascades/SOFT[6, 7, 8].pickle', 'rb'))

#[sizes1.append(siz) for siz in sizes2]
res = plot_cascade_sizes(sizes1,delays=[1,6],title='0.6',
                   filename='BA/images/cascades/full2_ratio3.png')

print(res)