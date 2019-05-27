import matplotlib.animation as anim
import networkx 
import matplotlib.pyplot as plt
import numpy as np
from time import sleep

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
        
        
c_elegans = networkx.read_weighted_edgelist(path="celegans_edges.txt")
n = c_elegans.number_of_nodes()

networkx.set_node_attributes(c_elegans,0,"infection")
for i in range(10):
    nod = np.random.randint(0,n)
    #print(nod)
    c_elegans.nodes[str(nod)]['infection']=1
        
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
pos = networkx.spring_layout(c_elegans)
colors = ['b','r']

for val in range(2) :

    list_nodes = [nodes for nodes in c_elegans.nodes
                                if c_elegans.nodes[nodes]['infection'] == val]
    networkx.draw_networkx_nodes(c_elegans, pos, list_nodes, node_size = 20,
                                node_color = colors[val])


networkx.draw_networkx_edges(c_elegans, pos, alpha=0.5)
    
def update(i):
    update_infection(c_elegans,0.2,0.4)
    
    ax.clear()
    for val in range(2) :

        list_nodes = [nodes for nodes in c_elegans.nodes
                                    if c_elegans.nodes[nodes]['infection'] == val]
        networkx.draw_networkx_nodes(c_elegans, pos, list_nodes, node_size = 20,
                                    node_color = colors[val])


    networkx.draw_networkx_edges(c_elegans, pos, alpha=0.5)
    sleep(0.3)
    
a = anim.FuncAnimation(fig, update, frames=70, repeat=False)
plt.show()