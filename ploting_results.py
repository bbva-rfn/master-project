import pickle
from plots_sis import plot_sectorial_multi_beta
from sis_delay_comparison import plot_comparison_densities
import numpy as np
from cascades import plot_cascade_sizes,lists_to_list

probs = pickle.load(open('BBVA/results/density_sectorialSOFT2.pickle', 'rb'))

names = {'0':'Financial Institutions' , '1':'Energy', '2':'Financial Services','3':'Utilities',
         '4':'Telecom','5':'Basic Materials','6':'Transportation','7':'Retail','8':'Retailers',
         '9':'Capital Goods','10':'Auto','12':'Construction and Infrastructure',
         '11':'Consumer and Healthcare','13':'Unknown','14': 'Real Estate' ,
         '15': 'Leisure','16':'Institutions','17':'Snow'}

betas = np.arange(0,1,0.1)
plot_sectorial_multi_beta(probs,names,betas,title='BBVA network with SOFT re-connection policy and delay 2',
                          filename='BBVA/images/sectorial_density.png')
'''

#densities = pickle.load(open('BBVA/results/comparison_ratio2_SOFT[1, 2, 3, 4, 5, 6, 7].pickle', 'rb'))
#densities2 = pickle.load(open('BBVA/results/comparison_ratio2_SOFT[8, 9].pickle', 'rb'))
#[densities.append(dens) for dens in densities2]
#plot_comparison_densities(densities,delays=[1,2,3,4,5],
 #                         filename='BBVA/images/comparison_final_ratio3_SOFT.png')


'''
'''
sizes1 = pickle.load(open('BBVA/results/cascades_ratio2_NONE[0].pickle', 'rb'))
#sizes2 = pickle.load(open('BBVA/results/cascades_ratio3_SOFT[2, 5].pickle', 'rb'))
#sizes3 = pickle.load(open('BBVA/results/cascades_ratio2_SOFT[5, 6].pickle', 'rb'))
#sizes4 = pickle.load(open('BBVA/results/cascades_ratio2_SOFT[7, 8].pickle', 'rb'))
sizes1 = [lists_to_list(sizes1)]
    
#[sizes1.append(siz) for siz in sizes2]
#[sizes1.append(siz) for siz in sizes3]
#[sizes1.append(siz) for siz in sizes4]
print(sizes1)
res = plot_cascade_sizes(sizes1,delays=['infty'],title='',ylim=10e-4,
                   filename='BBVA/images/cascades_control2.png')

print(res)
'''