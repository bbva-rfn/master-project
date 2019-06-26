from plots_sis import plot_sectorial_multi_beta,sectorial_multi_beta_paral
import pickle
import numpy as np
import time 



g = pickle.load(open('Barabasi-with-sectors2.pickle', 'rb'))


start = time.time()

probs = sectorial_multi_beta_paral(g,repetitions=12,default_delay=4,beta_lapse=0.05,num_sectors=5,
                                   filename='BA/results/sectorial_lapse005_',max_iterations=100)
end = time.time()
print(end - start)

betas = np.arange(0, 1, 0.05)

assert len(betas) == len(probs[0])

names = {'0':'Sector1' , '1':'Sector2', '2':'Sector3','3':'Sector4','4':'Sector5','5':'Sector6',
         '6':'Tallhart','7':'Dustin','8':'Reed','9':'Flynt','10':'Mormont','11':'Karstark',
         '12':'Cassel','13':'Poole','14': 'Frey'  ,'15': 'Tully','16':'Mallister','17':'Snow'}


plot_sectorial_multi_beta(probs,names,betas,filename='BA/images/sectorialSOFT4.png')


'''
probs = pickle.load(open('results/density/paral_provaSOFT2.pickle', 'rb'))
print(probs)
'''