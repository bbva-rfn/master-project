# -*- coding: utf-8 -*-
# analizing cascades

from cascades import plot_cascade_sizes,cascades_sizes_multiple,risk_cascades_sectorial
import pickle

g = pickle.load(open('graphs/new.pickle', 'rb'))
'''
Given a graph g, cascades_sizes_multiple computes for a mu and beta the cascades for several
delays with one policy. For statistical significance it has to be repeated several times, this
number of repetitions can be adjusted in the function. Also the maximum number of iterations
that the SIS can run can be passed too.
'''


sizes = cascades_sizes_multiple(g,beta=0.4,delays=[2,3,4,5],policy='RANDOM',repetitions=30)


''' plot_cascade_sizes plots the previously obtainned sizes, needs to now the used delays
and also requires the colors you want and the filename/path where to store the computed plot.
The ylim parameter allows to adjust the y-axis because in some plots it is not properly adjusted
but for an unknown result better to not use it.
'''


plot_cascade_sizes(sizes,delays=[2,3,4,5],ylim = 10e-4,colors=['r','g','b','k'],
                   filename='images/cascades/beta_0.4/comparison_RANDOM.png')



'''
Below we have sort of the risk per sector assessment based on the resultant cascades.
The parameters should be fined tunned with the BBVA data, actually putting the right number
of sectors.
Also take into consideration:
    amount_per_sector= number of nodes of every sector we consider randomly to perform the analysis
    repetitions_per_node = number of repetitions we do for every node of the cascades
    
Note that if there are 15 sectors, 10 nodes per sector considerer for the analysis
and 10 repetitions per node with two different delays this results in 3000 simulations !!!!!!!!

I did it for 3 sectors 5 repetitions per node and 10 nodes per sector with delays 2,4 to check
so 300 simulations and it worked in pretty decent time in my computer (less than 10 min). 
However a lot of simulations they may be. 
 '''
 
 
number_of_sectors = 3
delays_risk = [2,4]
maxim_prob,maximums = risk_cascades_sectorial(g,num_sectors = number_of_sectors,repetitions_per_node=5,
                                         beta=0.4,delays=delays_risk,amount_per_sector=10)

for i in range(number_of_sectors):
    print('For sector',i,'we have:')
    j = 0
    for delay in delays_risk:
        print('\nDelay',delay,'\n Maximum probable size of cascade',
              maxim_prob[i*len(delays_risk)+j],'\n Maximum size of the cascade',
              maximums[i*len(delays_risk)+j])
        j +=1
        