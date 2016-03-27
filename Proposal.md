# CAChemE Proposal

- *Submission Type:* 45 minutes
- *Title:* How to improve your diet and save money with Python
- *Subtitle (100 chars max):* Mathematical optimization with Pyomo or how to solve LP, NLP and MILP problems with Python
- *Sub Community:* Scientific 
- *Language:* English
- *Audience Level:* Beginner
- *Prerequisites for attending the session:* Python Basic Programming


## SHORT VERSION 
Optimization in Python (also known as mathematical programming) can be performed by minimization (or maximization) of an objective function within a model that can include discrete variables subject to a set of constrains. Optimization models are often described by specific algebraic modeling languages —mainly  [GAMS](http://www.gams.com/), [AMPL](http://ampl.com/) or [AIMMS](http://www.aimms.com/)— which are used in industry to solve different problems such as, equipment selection, scheduling, or supply chain of a company. [Pyomo](http://www.pyomo.org/) is an Open Source package —with an BSD licence from [Sandia National Laboratories](http://www.sandia.gov/), USA— developed in Python, which supports a different set of optimization capabilities in order to get a complet analysis and formulation of optimization problems. In particular, Pyomo can be applied in problems like [LP](https://en.wikipedia.org/wiki/Linear_programming), [QP](https://en.wikipedia.org/wiki/Quadratic_programming), [NP](https://en.wikipedia.org/wiki/Nonlinear_programming), MILP, MINLP, MISP among others. More importantly, pyomo models can communicate with principal commercial and open-source solvers; including [NEOS](http://www.neos-server.org/neos/) server platform. 
At this talk, Chemical Engineering students of the University of Alicante will introduce the audience to the possibilites of optimization, presenting Pyomo and showing real world examples such as how to improve your diet and save money at fast food restaurants.

## LONGER VERSION

Process optimization in industry has become essential in order to maximize the resources avaliable and reduce energy consumption. Modern industry is now trying to reduce its environmental impact by means of optimization tools. 
When one thinks about optimization in Computational Science, it is usually meant only to execution time reduction; but Mathematical Optimization (also known as the mathematical programming) has nothing to do with it. Nowadays, the education that many engineers and science students receive, limits solely to the SIMPLEX algorithm for Linear Problems with continuous variables. However, optimization problems become intersting when dealing with restrictions (linear or nonlinear) and integer variables (modeling the discrete decisions). Two of the most used commercial modeling languages to solve this problem sets are GAMS and AMPL. Python ecosystem presents different libraries to solve optimization problems, some of them are [CVXOpt](http://cvxopt.org/), [CVXPy](http://www.cvxpy.org/en/latest/), [PulP](https://pythonhosted.org/PuLP/), [OpenOpt](http://openopt.org/Welcome), or Pyomo. 
Among them, Pyomo results interesting because:
- It can be used for Mathematical modeling in Python simlarly to AMPL (and GAMS)
- It communicates with the main solvers used in this field such as GLPK, Gurobi, CPLEX, CBC and PICO
- It's free and open source Python library (BSD license), being developed by Sandia National Laboratories, USA.
- It supports Python 3 and it is easy install.
- It can use NEOS server (web platform which gives free access to commercial solvers)

In this way, Pyomo can compete with other commercial algebraic modelling languages such as AMPL, AIMMS and GAMS. Concretely, Pyomo can be used to model a variaty of mathematical models including: 

- Linear Programming
- Quadratic Programming
- Nonlinear Programming
- Linear Integer Mixed Programming
- Quadratic Integer Mixed Programming
- Linear Integer Mixed Programming
- Stochastic Integer Mixed Programming
- General Disjunctive Programming
- Differential algebraic equations 

The talk will be divided in three parts:

1. Introduction to Mathematical Programming/Optimization (15 min): visual introduction of optimization concepts including restrictions and non linearties (linear Programming, Nonlinear Programming, ILP, MIP, MINLP). 

2. Introduction to the Pyomo sintax and a quick note for the installation (20 min): showing how to improve their diet and save money when ordering food in fast food restaurants.
	
3. Optimization problems in Engineering (10 min): showing more adavanced optimization examples that include decision variables.

### About us:

[CAChemE](http://cacheme.org/) it's an nonprofit association formed by Chemical Engineers (professionals, students, and professors) which tries to encourage the new software possibilities in Chemical Process Engineering. Our goal is to promote the advantages of the Open Source alternatives such as Python and support their implementation at the university and industry. CAChemE is located in the [University Institute of Chemical Engineering Processes](http://iipq.ua.es/) at the [University of Alicante](http://www.ua.es/).

### Additional information for talk reviewers:

The talk will be oriented to beginners and will be given by Chemical Engineering students. Slides, Jupyter Notebooks will be available in GitHub.

*Tags:* Science Track, Educational Track, Scientific Libraries (maybe), Beginners, Engineering, Open-Source, Python 3, Jupyter/iPython Notebook, Python General, Science
