from plots_sis import plot_sectorial_multi_beta,sectorial_multi_beta_paral
import pickle
import numpy as np
import time 


g = pickle.load(open('graphs/new.pickle', 'rb'))
start = time.time()

probs = sectorial_multi_beta_paral(g,repetitions=5,default_delay=2,beta_lapse=0.05,
                                   filename='results/density/paral_prova',max_iterations=100)
end = time.time()
print(end - start)

betas = np.arange(0, 1, 0.05)
assert len(betas) == len(probs[0])

names = {'0':'Stark' , '1':'Bolton', '2':'Umber','3':'Manderly','4':'Hornwood','5':'Glover',
         '6':'Tallhart','7':'Dustin','8':'Reed','9':'Flynt','10':'Mormont','11':'Karstark',
         '12':'Cassel','13':'Poole','14': 'Frey'  ,'15': 'Tully','16':'Mallister','17':'Snow'}

plot_sectorial_multi_beta(probs,names,betas,filename='images/density/paral_prova5.png')

'''
probs = pickle.load(open('results/density/paral_provaSOFT2.pickle', 'rb'))
print(probs)
'''