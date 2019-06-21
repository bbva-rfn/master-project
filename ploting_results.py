import pickle

import time
from sis_delay_comparison import plot_comparison_densities

d1 = pickle.load(open('ER/results/comparison_ratio3_RANDOM[1, 3, 5].pickle', 'rb'))
d2 = pickle.load(open('ER/results/comparison_ratio3_RANDOM[2, 4, 6].pickle', 'rb'))
#d3 = pickle.load(open('ER/results/comparison_ratio3_SOFT[9, 10, 11].pickle', 'rb'))
start = time.time()

for d in d2:
    d1.append(d)
'''
for d in d3:
    d1.append(d)
'''
plot_comparison_densities(d1, title='RANDOM policy', delays=[1, 3, 5, 2, 4, 6],
                          filename='ER/images/delay_comparison2_RANDOM3.png')

end = time.time()
