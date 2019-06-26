from cascades import full_check_cascade_size_setting_default
import pickle

#all should be done for beta 0.4,0.6 
#all for SOFT policy
#for BA node_id 0,7, 70
#for ER node_id 871,899
#for BBVA node_id 1,
#delay = 5 and 6 for beta 0.4
#delay = 3 for beta = 0.6
#The function only allows for 1 delay at a time but it is parellizes the number of repetitions
graph = pickle.load(open('BA/Barabasi-with-sectors.pickle', 'rb'))
siz = full_check_cascade_size_setting_default(graph,node_id=0,mu=0.2,beta=0.4,repetitions=60,
                                              delay=5,policy='SOFT',
                                              filename='BA/results/risk_')
