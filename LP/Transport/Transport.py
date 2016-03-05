#Author: [Carlos Planelles](https://github.com/Planelles20)

from __future__ import division
from pyomo.environ import *

model = AbstractModel()

#sets
model.I = Set() #mercados
model.J = Set() #plantas

#parametros
model.D = Param(model.I)
model.P = Param(model.J)
model.A = Param(model.J, model.I)
model.f = Param()

#variables
model.x = Var(model.J, model.I, domain=NonNegativeReals)

#funcion objetivo

def objfunc(model):
    return model.f*summation(model.A, model.x)

model.OBJ = Objective(rule=objfunc, sense=minimize)

#constraint
def const1(model, i):
    return sum(model.x[j,i] for j in model.J) >= model.D[i]

model.CONST1 = Constraint(model.I, rule=const1)

def const2(model, j):
    return sum(model.x[j,i] for i in model.I) <= model.P[j]

model.CONST2 = Constraint(model.J, rule=const2)
