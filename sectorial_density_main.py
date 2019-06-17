from plots_sis import sectorial_multi_beta,plot_sectorial_multi_beta,sectorial_multi_beta_paral
import pickle
import numpy as np

g = pickle.load(open('graphs/new.pickle', 'rb'))

probs = sectorial_multi_beta_paral(g,repetitions=2,default_delay=2,beta_lapse=0.1)

betas = np.arange(0, 1, 0.1)
assert len(betas) == len(probs[0])

names = dict(np.arange(17))
plot_sectorial_multi_beta(probs,names,betas)