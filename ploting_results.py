import pickle
from plots_sis import plot_sectorial_multi_beta
from sis_delay_comparison import plot_comparison_densities
import numpy as np
from cascades import plot_cascade_sizes


probs = pickle.load(open('BA/results/sectorial_provaSOFT4.pickle', 'rb'))

names = {'0':'Sector 1' , '1':'Sector 2', '2':'Sector 3','3':'Sector 4','4':'Sector 5','5':'Glover',
         '6':'Tallhart','7':'Dustin','8':'Reed','9':'Flynt','10':'Mormont','11':'Karstark',
         '12':'Cassel','13':'Poole','14': 'Frey'  ,'15': 'Tully','16':'Mallister','17':'Snow'}

betas = np.arange(0,1,0.4)
plot_sectorial_multi_beta(probs,names,betas,title='BA network',
                          filename='BA/images/sectorial_density1.png')
'''

densities = pickle.load(open('BBVA/results/comparison_ratio2_SOFT[1, 2, 3, 4, 5, 6, 7].pickle', 'rb'))
densities2 = pickle.load(open('BBVA/results/comparison_ratio2_SOFT[8, 9].pickle', 'rb'))
[densities.append(dens) for dens in densities2]
plot_comparison_densities(densities,delays=[1,2,3,4,5,6,7,8,9],
                          filename='BBVA/images/comparison_final_ratio2_SOFT.png')


'''
'''
sizes1 = pickle.load(open('BA/results/cascades/SOFT[1, 6].pickle', 'rb'))
sizes2 = pickle.load(open('BA/results/cascades/ratio3_SOFT[2, 3, 4, 5].pickle', 'rb'))


[sizes1.append(siz) for siz in sizes2]

res = plot_cascade_sizes(sizes1,delays=[1,6,2,3,4,5],title='0.6',ylim=10e-4,
                   filename='BA/images/cascades/full2_ratio3.png')

print(res)
'''