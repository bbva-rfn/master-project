# -*- coding: utf-8 -*-
# risk functions implementation

from risk_functions import *
import pickle

g = pickle.load(open('graphs/new.pickle', 'rb'))
risk_for_me(g,4)

print('Yeah!')