# -*- coding: utf-8 -*-
# risk functions implementation

from risk_functions import risk_for_me_one,risk_for_me_one_strict,risk_for_me_some
import pickle

g = pickle.load(open('graphs/new.pickle', 'rb'))
'''
with nodes 4,7 I obtain risk 1 in both, curious 

we try now 4,117 and also risk 1 as it says first defaulted at 0
Problem!
Solved the problem
now it gives 0 for lax risk and 0.5 for strict which is nice for 2 repetitions a study 
should be performmed
'''
'''
risk = risk_for_me_one(g,4,117,repetitions=2)
print("Lax risk",risk)
risk = risk_for_me_one_strict(g,4,117,repetitions=2)
print("Strict risk",risk)
'''

risk = risk_for_me_some(g,4,[7,117,45,23],repetitions=3)
print("Risk",risk)
