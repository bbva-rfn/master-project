import pickle

sn = pickle.load(open('results/sto_random_weights.pickle', 'rb'))
sn.plot()
