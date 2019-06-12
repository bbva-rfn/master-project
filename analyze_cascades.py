# -*- coding: utf-8 -*-
# analizing cascades
'''
from cascades import full_check_cascade_size_recursive,cascade_size_plot

sizes = full_check_cascade_size_recursive(repetitions=2,delay=2)
print(sizes)

cascade_size_plot(sizes,1000,filename='images/cascade_plot_delay2.png')

delays = [2,4,6]

for delay in delays:
    sizes = full_check_cascade_size_recursive(delay=delay,show=False)
    print(sizes)
    name = 'images/cascade_plot_delay'+str(delay)+'.png'
    cascade_size_plot(sizes,1000,filename=name)
    print('One less')

print('Yeah!')
'''

'''
from cascades import nice_cascade_plot_comparison

nice_cascade_plot_comparison(repetitions=25,
                             beta=0.5,
                             delays=[2, 3, 4, 5],
                             colors = ['r','b','g','k'],
                             policy='SOFT',
                             filename='images/cascades/beta_0.5/comparison_SOFT.png')

'''

from cascades import plot_cascade_sizes,cascades_sizes_multiple
import pickle

g = pickle.load(open('graphs/new.pickle', 'rb'))

sizes = cascades_sizes_multiple(g,delays=[2,4])
plot_cascade_sizes(sizes,delays=[2,4])
