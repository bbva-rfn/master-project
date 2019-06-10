# -*- coding: utf-8 -*-
#analizing cascades

from cascades import *

sizes = full_check_cascade_size_recursive(repetitions=2,delay=4)
print(sizes)

cascade_size_plot(sizes,1000)

print('Yeah!')