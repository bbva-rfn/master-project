# master-project

This repository is a collection of Jupyter notebooks intended to solve a lot of problems in which we want to predict a probability distribution by using Mixture Density Network avoiding a NaN problem and other derived problems of the model proposed by Bishop, C. M. (1994). The second major objective of this repository is to look for ways to predict uncertainty by using artificial neural networks.

The whole code, until 20.1.2017, is the result of a final Master's Thesis of the Master's Degree in Artificial Intelligence supervised by Jordi Vitrià, PhD. The Master's Thesis report is published in this repository in a PDF format but my idea is to realize a web view of the final master's work in the coming days. To summary all the contents I explained in the report, it is possible to consult the slides of the presentation. Any contribution or idea to continue the lines of the proposed work will be very welcome.


Team member contribution

In this section we describe the contribution of each member to the overall project. We will divide it in two groups, code and report. 

Code

The contributions for the code have been:

   - Philippe Van Ameronggen
 
       -  Main algorithm that simulates the SIS behaviour with the different agents and policies described. (SecNet.py)
        
        - BBVA simulated network generation. (BBVA/gen.py)
        
        - Parallelization of all the functions to use the multiple cores of a machine.
        
        - High level overview
        
        - Agent-based model implementations
        
    
    
   - Ramon Mir Mora
    
        
        -  Functions that use the main algorithm to compute some the results in \ref{Results}. Mainly, all the failure cascades/risk code (cascades.py), the average default density evolution compared over multiple delays (sis\_delay\_comparison.py) and the sectorial behaviour (sectorial\_density\_functions.py and the sectorial part in plots\_sis.py). 
        
        - ER and BA model networks generation. (gen.py in each folder)
        
        - Agent-based model implementations
        
      
    
   - Sergi Sánchez de la Blanca Contreras
    
        
        - Code to perform the Monte-Carlo simulations (replicate\_density.py and the rest of plots\_sis.py) 
        
        -  All the Simulation execution 
        
        - Agent-based model implementations
        
       -  Refining and cleaning code
        



Report

Here we stipulate the contributions of each member to the present report. 


 - Philippe Van Ameronggen

     - Narrative parts (Abstract,Introduction,Study Design,Discussions)

 - Ramon Mir Mora


     - Theoretical parts (Complex Networks, SIS model,Failure Cascades)

     - Results analysis (Cascades, risks and ER-BA comparison)

     - Conclusions and Appendix B



 - Sergi Sánchez de la Blanca Contreras


     - Database/previous work explanation/  Study Design

     - Results, execution \& analysis (Study of critical delay ER-BA)

     - Appendix A


Notebooks

(Currently programed on Spider Python 3.6 )

Contributions

Contributions are welcome! For bug reports or requests please submit an issue.

Contact

Feel free to contact me to discuss any issues, questions or comments.

GitHub: aemon4,phicoder,Sergisanchezcontreras
Website: https://github.com/bbva-rfn/master-project/edit/master/README.md

License

The content developed by Axel Brando is distributed under the following license:

Copyright 2018 Sergi Sánchez de la blanca Contrera, Philippe Van Amerongen, Ramon Mir Mora

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

