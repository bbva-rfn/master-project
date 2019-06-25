import pickle
from plots_sis import plot_sectorial_multi_beta
import numpy as np

'''
probs = pickle.load(open('BBVA/results/density_sectorialSOFT2.pickle', 'rb'))

names = {'0':'Stark' , '1':'Bolton', '2':'Umber','3':'Manderly','4':'Hornwood','5':'Glover',
         '6':'Tallhart','7':'Dustin','8':'Reed','9':'Flynt','10':'Mormont','11':'Karstark',
         '12':'Cassel','13':'Poole','14': 'Frey'  ,'15': 'Tully','16':'Mallister','17':'Snow'}

betas = np.arange(0,1,0.1)
plot_sectorial_multi_beta(probs,names,betas,filename='BBVA/images/sectorial_density1.png')
'''

probs = pickle.load(open('BBVA/results/density_sectorialSOFT2.pickle', 'rb'))