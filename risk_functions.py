#risk functions for assessments

from networkx import DiGraph
from SecNet import SecNet, ReconnectionPolicy
import numpy as np

def set_initial_defaults(graph:DiGraph,node_id):
    for node_i in graph:
        node = graph.nodes[node_i]
        if node['id'] == node_id:
            node['defaulted'] = 1
        else:
            node['defaulted'] = 0

def set_initial_defaults_several(graph:DiGraph,node_ids:list):
    for node_id in graph:
        node = graph.nodes[node_id]
        if node_id in node_ids:
            node['defaulted']=1
        else:
            node['defaulted']=0
        
def risk_for_me_all(graph:DiGraph,node_id,iterations=70,mu=0.2,beta=0.6,delay=2,weight_transfer=False):
    risks = []
    for node_i in graph:
        node = graph.nodes[node_i]
        if node['id'] != node_id:
            set_initial_defaults(graph,node['id'])
            sn = SecNet(graph, mu, beta, reconnection_policy=ReconnectionPolicy.RANDOM, default_delay=delay, weight_transfer=weight_transfer)
            sn.run(iterations)
            #sn.run(5)
            #for i in range(iterations):
             #   if(sn.defaulted_density[-1]>0):
              #      sn.run(1)
               # else:
                #    break
            risks.append([node['id'],sn.graph.nodes[node_id]['first_defaulted_at']])
    for lis in risks:
        if(lis[1]==-1):
            lis[1]=0
        else:
            lis[1] = 1.-lis[1]/100.
    return risks

def risk_for_me_one(graph:DiGraph,node_id_me,node_id_other,repetitions=20,iterations=100,
                    mu=0.2,beta=0.6,delay=2,weight_transfer=False):
    risks = []
    for i in range(repetitions):
        set_initial_defaults(graph,node_id_other)
        sn = SecNet(graph, mu, beta, reconnection_policy=ReconnectionPolicy.RANDOM,
                    default_delay=delay, weight_transfer=weight_transfer)
        sn.run(iterations)
        risk = sn.graph.nodes[node_id_me]['first_defaulted_at']
        #print(risk)
        #print(sn.graph.nodes[node_id_me])
        '''for node_id in sn.graph.nodes:
            node = sn.graph.nodes[node_id]
            print(node['first_defaulted_at'])
         '''   
        if risk == -1:
            risk = 0
        else:
            risk = 1.-float(risk/iterations)
        risks.append(risk)
    return np.mean(risks)

def risk_for_me_one_strict(graph:DiGraph,node_id_me,node_id_other,repetitions=20,
                           iterations=100,mu=0.2,beta=0.6,delay=2,weight_transfer=False):
    
    risks = []
    for i in range(repetitions):
        set_initial_defaults(graph,node_id_other)
        sn = SecNet(graph, mu, beta, reconnection_policy=ReconnectionPolicy.RANDOM,
                    default_delay=delay, weight_transfer=weight_transfer)
        sn.run(iterations)
        risk = sn.graph.nodes[node_id_me]['first_defaulted_at']
        if risk == -1:
            risk = 0
        else:
            risk = 1
        risks.append(risk)
    return np.mean(risks)


def risk_for_me_some(graph:DiGraph,node_id_me,node_id_others:list,repetitions=20,
                           iterations=100,mu=0.2,beta=0.6,delay=2,
                           weight_transfer=False,strict=False):
    risks = []
    for i in range(repetitions):
        set_initial_defaults_several(graph,node_id_others)
        sn = SecNet(graph, mu, beta, reconnection_policy=ReconnectionPolicy.RANDOM,
                    default_delay=delay, weight_transfer=weight_transfer)
        sn.run(iterations)
        risk = sn.graph.nodes[node_id_me]['first_defaulted_at']
        if risk == -1:
            risk = 0
        else:
            if(strict):
                risk = 1
            else:
                risk = 1-float(risk/iterations)
        risks.append(risk)
    return np.mean(risks)


def risk_overall(graph:DiGraph,repetitions=10,iterations=75,mu=0.2,beta=0.6,delay=2,
                 weight_transfer=False):
    #we need an atribute that is risk_overall 
    for node_id in graph:
        node = graph.nodes[node_id]
        set_initial_defaults(graph,node['id'])
        sn = SecNet(graph, mu, beta, reconnection_policy=ReconnectionPolicy.RANDOM, default_delay=delay, weight_transfer=weight_transfer)
        sn.run(iterations)
    return 'Done'
        
    
    
        