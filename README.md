# Agent-based models for assessing the risk of default propagation in interconnected sectorial financial networks

This project is a continuation of Barja et al., [2019](#references) and aims to provide more accurate insights in risk assessment of default propagation in interconnected sectorial financial networks. The algorithm may be used to analyze systemic risk posed by companies on a financial system, as well as to assess the global stability of a financial system. 

The financial system is modelled by using transaction data between businesses. The transaction data is then converted into client-supplier relationships, represented as a directional weighted graph. The Python3 library [networkx](https://networkx.github.io/) is used for efficient graph management.

The code, until 1 July 2019, is a product of the Master's Thesis, part of the Master's Degree in Data Science at the Universitat de Barcelona supervised by Jordi Nin, PhD.

## Code structure and usage

Explain code structure and usage

Ramon: I'll write the main functions that a user can use to compute things on their networks

All the functions allow the following parameters as input: 
- Graph: Your financial client-supplier network 
- Mu: The value of the recovery rate
- Beta: The value of the infetious rate
- Max_iterations/Iterations: The maximum number of iterations the algorithm may run for every simulation
- Repetitions: The amount of simulations we want to do from scratch
- Delay: The value or values of the parameter delay
- Policy: The underlying policy we want our system to follow: 'SOFT','RANDOM','NONE'
- Filename: Where to store the computed values. The filename is completed inside the functions with the policy and the delay, be carefull. 

1. To compute the default probability behaviour:

In sis_delay_comparison.py:
- compare_density() , gives the average default density behaviour of all the computed simulations for every delay given in a list of lists.
- plot_comparison_densities() allows you to plot the previously obtainned densities

In sectorial_density_functions.py:
- density_with_sigma(), returns all the values of the density at each iteration for all the simulations performed in a pandas dataframe.
It allows to give a more detailed plot of the average default density for one delay including the confidence interval.In this case the reconnection policy uses the defined class ReconnectionPolicy.SOFT,.NONE,...
- plot_density_sigm()a: allows you to plot the previous density
  
2. To analyze the cascades and risk:
From cascades.py:
- cascades_sizes_multiple(), returns the cascade sizes of all the resultant cascades in a list of lists. Every list corresponds to one inputed delay.
- full_check_cascade_size_setting_default(), allows to check the sizes of the cascades when setting one node(extra parameter: node_id) to default for one single delay.
- plot_cascade_sizes(), plots the list of lists that contains the sizes obtainned with the functions before. The function also returns the expected cascade size and the maximum cascade size for every delay in the format (delay,expected cascade size,maximum cascade size).
To plot the sizes of single delay returned with full_check_cascade_size_setting_default() it might be necessary to apply the function lists_to_list() to the result. This function is also in cascades.py()

There are more functions that allow to do the sectorial computations and compute more types of risks unused in our project. But mainly this is the basic functions to perform an analysis of your client-supplier network. 
## Contact

Feel free to contact us to discuss any issues, questions or comments.

GitHub: [Ramon Mir](https://github.com/aemon4), [Philippe van Amerongen](https://github.com/phicoder), [Sergi Sánchez](https://github.com/Sergisanchezcontreras)

### BibTex reference format for citation for the Code
```
@misc{BBVArfn_code,
title={Agent-based models for assessing the risk of default propagation in interconnected sectorial financial networks},
url={https://github.com/bbva-rfn/master-project},
note={GitHub repository with a collection of code intended to simulate financial client-supplier networks.},
author={Philippe van Amerongen, Ramon Mir Mora, Sergi Sánchez de la blanca Contreras},
year={2019}
}
```

### BibTex reference format for citation for the report of the Master's Thesis
```
@misc{BBVArfn,
title={Agent-based models for assessing the risk of default propagation in interconnected sectorial financial networks},
url={https://github.com/bbva-rfn/master-project/blob/master/_thesis.pdf},
author={Philippe van Amerongen, Ramon Mir Mora, Sergi Sánchez de la blanca Contreras},
year={2019}
}
```
## License

The content developed by Philippe van Amerongen, Ramon Mir Mora and Sergi Sánchez de la blanca Contreras is distributed under the following license:

```
MIT License

Copyright (c) 2019 Philippe van Amerongen, Ramon Mir Mora, Sergi Sánchez de la blanca Contreras

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## References
Adrià Barja, Alejandro Martínez, Alex Arenas, Pablo Fleurquin, Jordi Nin, José J. Ramasco and Elena Tomás (2019). "Assessing the Propagation of Default in Intercon-nected Sectorial Financial Networks." In: *IEEE COMPUTATIONAL INTELLIGENCE MAG.*