# CAChemE Proposal

- *Submission Type:* 45 minutes
- *Title:* Mathematical Optimization with Pyomo
- *Subtitle (100 chars max):* Usage of Pyomo to solve different Optimization Problems (LP, NLP, QP, MILP, MINLP and MISP)
- *Sub Community:* All 
- *Language:* English
- *Audience Level:* Beginner
- *Prerequisites for attending the session:* Python Basic Programming


## SHORT VERSION 
Optimization or Mathematical Programming with different algebraic modeling languages -- better known as [GAMS](http://www.gams.com/), [AMPL](http://ampl.com/) and [AIMMS](http://www.aimms.com/) --- is used in the Industry to solve different problems, covering problems as the selection of the perfect equipment or the logistical management of a Company. [Pyomo](http://www.pyomo.org/) is an Open Source package -- with an BSD licence from [Sandia National Laboratories](http://www.sandia.gov/), USA--- developed in Python, which supports a different set of optimization capabilities in order to get a complet analysis and formulation of the Optimization problems. In particular, Pyomo can be applied in problems like [LP](https://en.wikipedia.org/wiki/Linear_programming), [QP](https://en.wikipedia.org/wiki/Quadratic_programming), [NP](https://en.wikipedia.org/wiki/Nonlinear_programming), MILP, MINLP, MISP and a lot of others. Another plus is that it can be linked with the principal commercial solvers, open code and/or free solvers, like the  [NEOS](http://www.neos-server.org/neos/) server platform. 
At this talk, Chemical Engineering students of the University of Alicante will show a visual introduction of the optimization world, presenting Pyomo and the resolution of practical cases.

## LONGER VERSION

The process optimization at the Industry sector has been growing in the last years. The modern industry use it in a lot of different fields, you can find it at the optimization of the production, to reduce the costs, to reduce the environmental impact or to increase the security sector. So it`s reasonable to introduce and educate new engineers at this science sector.  

When you think about Optimization at the world of the Computational Science, normally, people refer to it to reduce the execution time of the code; but Mathematical Optimization (also known as the mathematical programming) has nothing to do with it, and in a lot of cases the education we receive remains at the SIMPLEX algorithm for Linear Problems with continuous variables.  

An Optimization problem consists, roughly speaking, in the maximization or minimization of a real function choosing the init values systematically (taking a permitted set) and calculating the function value. This problem gets interesting when we have to deal with restrictions (linear or nonlinear) and integer variables (modeling the discrete decisions). Two of the most used commercial modeling languages to solve this problem sets are GAMS and AMPL. Python has a lot of different libraries to solve the same type of problems, some of them are [CVXOpt](http://cvxopt.org/), [CVXPy](http://www.cvxpy.org/en/latest/), [PulP](https://pythonhosted.org/PuLP/), [OpenOpt](http://openopt.org/Welcome), or Pyomo. The last one, Pyomo.org, results interesting because:
- It can be used for Mathematical modelling in Python like AMPL/GAMS
- It can be linked directly with the principal solvers, as well as GLPK, Gurobi, CPLEX, CBC y PICO
- It's open source (BSD license) and the developer is Sandia National Laboratories, USA.
- Pyomo (older days known as Coopr) is 100% free, mature and well documented.
- It has a Python 3  support and a easy installation.
- It can use NEOS server (web platform which gives access to the commercial solvers -- for free)
- It's developed in Python, so it can be adapted to different types a problem models.

Pyomo shows, that it can compete with other commercial algebraic modelling languages as AMPL, AIMMS and GAMS, but it has the benefit that it's in Python, an high level programming skill with a wide spectrum of scientific libraries. Taking reference to the capabilities like a algebraic modeling language, Pyomo is able to embrace a lot of different problem types, including some like: 

- Linear Programming
- Quadratic Programming
- Nonlinear Programming
- Linear Integer Mixed Programming
- Quadratic Integer Mixed Programming
- Linear Integer Mixed Programming
- Stochastic Integer Mixed Programming
- General Disjunctive Programming
- Differential algebraic equations 

The talk is divided in three parts:

1. Introduction to Mathematical Programming/Optimization (15 min): it is a visual introduction of the Optimization concepts with restrictions (linear Programming, Nonlinear Programming, ILP, MIP, MINLP). 

2. Introduction to the Pyomo syntaxes and a quick note for the installation (15min): 	it will be focused on simple optimization examples solved with Pyomo. 	
	
3. Optimization problems  in Engineering  (15 min): 	taking special attention of solved examples of the real life.

### About us:

[CAChemE](http://cacheme.org/) it's an nonprofit association formed by Chemical Engineers (professionals, teachers and students) which tries to encourage the software possibilities at the Chemical Process Engineering. Our goal is to promote the advantages of the new Open Source software tools and promote their use at the University and Industry. The headquarter of CAChemE is in the [University Institute of Chemical Engineering Processes](http://iipq.ua.es/) at the [University of Alicante](http://www.ua.es/).

### Additional information for talk reviewers:

The talk will be oriented to beginners and will be given by three Chemical Engineering students. Therefore,  it will be given for granted that the audience know the basic concepts about programming with Python. The code of the solved problems and the slideshow will be available on our GitHub repo.

** Tags: ** Science Track, Educational Track, Scientific Libraries (maybe), Beginners, Engineering, Open-Source, Python 3, Jupyter/iPython Notebook, Python General, Science
