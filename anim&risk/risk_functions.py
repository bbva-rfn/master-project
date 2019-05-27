#risk assessment with also simple functions just for a glimpse at the idea
import networkx 
import numpy as np


def update_infection_sing(node,graph,mu,beta):
    node_id = str(node)
    infec = graph.nodes[node_id]['infection']
    neigh = graph.neighbors(node)

    q = calculate_q(neigh,graph,beta)
    new_infec = (1 - q) * (1 - infec) + (1 - mu) * infec + mu * (1 - q) * infec
    
    new_infec = 1 if np.random.random() < new_infec else 0
    graph.nodes[node_id]['infection']= new_infec
    
def calculate_q(nodes,graph,beta):
    infections = []
    r = 0
    for node in nodes:
        node_id = str(node)
        infections.append(graph.nodes[node_id]['infection'])
        r+=1
    r = 1./r
    infections = np.array(infections)
    return np.prod(1 - beta * r * infections)

def update_infection(graph,mu,beta):
    for node in graph.nodes:
        update_infection_sing(node,graph,mu,beta)
        
def sis_algo_risk(graph,max_iterations = 75,mu=0.2,beta=0.4):
    equilibrium = mu/beta
    n = graph.number_of_nodes()
    for i in range(max_iterations):
        total_inf = 0
        for node in graph.nodes:
            total_inf += graph.nodes[str(node)]['infection']
        total_inf = total_inf/n
        if(total_inf > equilibrium):
            return i
        elif(total_inf == 0):
            return max_iterations
        else:
            update_infection(graph,mu,beta)
        
    return i

def risk_assessment(graph,mu=0.2,beta=0.4,max_iterations=150,repetitions = 100):
    networkx.set_node_attributes(graph,0,"risk")
    #we assume a maximum risk of 1, and minimum of 0 and risk is inversament proporcional to the amount of iterations that
    #it takes to surpass the equilibrium state the first time
    for node in graph.nodes:
        aux_risk = np.zeros(repetitions)
        
        for j in range(repetitions):
            networkx.set_node_attributes(graph,0,"infection")
            graph.nodes[node]['infection']= 1

            i = sis_algo_risk(graph,max_iterations,mu,beta)
            aux_risk[j] = 1-i/max_iterations
            
        graph.nodes[node]["risk"]= np.mean(aux_risk)
        #print(node)
        
        