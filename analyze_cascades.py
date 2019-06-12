# -*- coding: utf-8 -*-
#analizing cascades
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

from cascades import nice_cascade_plot_comparison

nice_cascade_plot_comparison(repetitions=25,
                             delays = [2,3,4],
                             filename='images/nice_cascade_comparison2.png')

