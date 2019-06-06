#risk functions for assessments

from networkx import DiGraph
from SecNet import SecNet, ReconnectionPolicy


def set_initial_defaults(graph:DiGraph,node_id):
    for node_id in graph:
        node = graph.nodes[node_id]
        if node['id'] == node_id:
            node['defaulted'] = 1
        else:
            node['defaulted'] = 0

    
def risk_for_me(graph:DiGraph,node_id,iterations=70,mu=0.2,beta=0.6,delay=2,weight_transfer=False):
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

def risk_overall(graph:DiGraph,repetitions=10,iterations=75,mu=0.2,beta=0.6,delay=2,weight_transfer=False):
    #we need an atribute that is risk_overall 
    for node_id in graph:
        node = graph.nodes[node_id]
        set_initial_defaults(graph,node['id'])
        sn = SecNet(graph, mu, beta, reconnection_policy=ReconnectionPolicy.RANDOM, default_delay=delay, weight_transfer=weight_transfer)
        sn.run(iterations)
    return 'Done'
        
    
    
        