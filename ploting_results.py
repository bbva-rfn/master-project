import pickle
from plots_sis import plot_sectorial_multi_beta
from sis_delay_comparison import plot_comparison_densities
import numpy as np
from cascades import plot_cascade_sizes

'''
probs = pickle.load(open('BA/results/sectorial_provaSOFT4.pickle', 'rb'))

names = {'0':'Sector 1' , '1':'Sector 2', '2':'Sector 3','3':'Sector 4','4':'Sector 5','5':'Glover',
         '6':'Tallhart','7':'Dustin','8':'Reed','9':'Flynt','10':'Mormont','11':'Karstark',
         '12':'Cassel','13':'Poole','14': 'Frey'  ,'15': 'Tully','16':'Mallister','17':'Snow'}

betas = np.arange(0,1,0.4)
plot_sectorial_multi_beta(probs,names,betas,title='BA network',
                          filename='BA/images/sectorial_density1.png')


densities = pickle.load(open('BBVA/results/comparison_ratio3_SOFT[1, 2, 3, 4, 5].pickle', 'rb'))
#densities2 = pickle.load(open('BBVA/results/comparison_ratio2_SOFT[8, 9].pickle', 'rb'))
#[densities.append(dens) for dens in densities2]
plot_comparison_densities(densities,delays=[1,2,3,4,5],
                          filename='BBVA/images/comparison_final_ratio3_SOFT.png')


'''

sizes1 = pickle.load(open('BBVA/results/cascades_ratio3_SOFT[1, 2, 3, 4].pickle', 'rb'))
sizes2 = pickle.load(open('BBVA/results/cascades_ratio3_SOFT[2, 5].pickle', 'rb'))
#sizes3 = pickle.load(open('BBVA/results/cascades_ratio2_SOFT[5, 6].pickle', 'rb'))
#sizes4 = pickle.load(open('BBVA/results/cascades_ratio2_SOFT[7, 8].pickle', 'rb'))
i = 0
for siz in sizes2:
    if(i!=0):
        sizes1.append(siz)
    i+=1
    
#[sizes1.append(siz) for siz in sizes2]
#[sizes1.append(siz) for siz in sizes3]
#[sizes1.append(siz) for siz in sizes4]

res = plot_cascade_sizes(sizes1,delays=[1,2,3,4,5],title='',ylim=10e-4,
                   filename='BBVA/images/cascades_compa2_ratio3.png')

print(res)
