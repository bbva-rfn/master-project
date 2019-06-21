import pickle

import time
from sis_delay_comparison import plot_comparison_densities

d1 = pickle.load(open('ER/results/comparison_ratio2_SOFT[1, 3, 5, 7].pickle', 'rb'))
d2 = pickle.load(open('ER/results/comparison_ratio2_SOFT[2, 4, 6, 8].pickle', 'rb'))
d3 = pickle.load(open('ER/results/comparison_ratio2_SOFT[9, 10, 11].pickle', 'rb'))
start = time.time()

for d in d2:
    d1.append(d)

for d in d3:
    d1.append(d)

plot_comparison_densities(d1, title='SOFT policy', delays=[1, 3, 5, 7, 2, 4, 6, 8, 9, 10, 11],
                          filename='ER/images/delay_comparison2_SOFT2.png')

end = time.time()
