import pickle
from SecNet import SecNet

g = pickle.load(open('graphs/new.pickle', 'rb'))
sn = SecNet(g, 0.4, 0.5)
sn.run(100)
pickle.dump(sn, open('results/test.pickle', 'wb'))
