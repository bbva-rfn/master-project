import pickle

import time
from sis_delay_comparison import plot_comparison_densities

d1 = pickle.load(open('ER/results/comparison2_ratio2_RANDOM[3, 5, 7].pickle', 'rb'))
d2 = pickle.load(open('ER/results/comparison2_ratio2_RANDOM[2, 4, 8].pickle', 'rb'))
d3 = pickle.load(open('ER/results/comparison2_ratio2_RANDOM[9, 10, 11].pickle', 'rb'))
d4 = pickle.load(open('ER/results/comparison2_ratio2_RANDOM[1, 6].pickle', 'rb'))
start = time.time()

for d in d2:
    d1.append(d)

for d in d3:
    d1.append(d)

for d in d4:
    d1.append(d)
plot_comparison_densities(d1, title='RANDOM policy', delays=[3, 5, 7, 2, 4, 8, 9, 10, 11,1],
                          filename='ER/images/delay_comparison_RANDOM2.png')

end = time.time()
