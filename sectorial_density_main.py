from plots_sis import sectorial_multi_beta,plot_sectorial_multi_beta,sectorial_multi_beta_paral
import pickle
import numpy as np

g = pickle.load(open('graphs/new.pickle', 'rb'))

probs = sectorial_multi_beta_paral(g,repetitions=3,default_delay=2,beta_lapse=0.2,
                                   filename='results/density/paral_prova')

betas = np.arange(0, 1, 0.2)
assert len(betas) == len(probs[0])

names = {'0':'Stark' , '1':'Bolton', '2':'Umber','3':'Manderly','4':'Hornwood','5':'Glover',
         '6':'Tallhart','7':'Dustin','8':'Reed','9':'Flynt','10':'Mormont','11':'Karstark',
         '12':'Cassel','13':'Poole','14': 'Frey'  ,'15': 'Tully','16':'Mallister','17':'Snow'}

plot_sectorial_multi_beta(probs,names,betas,filename='images/density/prova2.png')

'''
probs = pickle.load(open('results/density/paral_provaSOFT2.pickle', 'rb'))
print(probs)
'''