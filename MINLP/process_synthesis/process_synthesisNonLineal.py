#Author: [Carlos Planelles](https://github.com/Planelles20)

from __future__ import division
from pyomo.environ import *

model = ConcreteModel()

M = 10

model.yI   = Var(within=Binary)
model.yII  = Var(within=Binary)
model.yIII = Var(within=Binary)

model.CosteI   = Var()
model.CosteII  = Var()
model.CosteIII = Var()

model.AI   = Var(domain=NonNegativeReals)

model.Bext = Var(domain=NonNegativeReals)
model.BI   = Var(domain=NonNegativeReals)
model.BII  = Var(domain=NonNegativeReals)
model.BIII = Var(domain=NonNegativeReals)

model.C    = Var(domain=NonNegativeReals)
model.CII  = Var(domain=NonNegativeReals)
model.CIII = Var(domain=NonNegativeReals)

#constraints

model.ConstI1 = Constraint(expr=(model.CosteI == 250*model.AI+1000*model.yI))
model.ContsI2 = Constraint(expr=(model.BI == 0.9*model.AI))
model.ContsI3 = Constraint(expr=(model.AI <= 40*model.yI))

model.ConstII1 = Constraint(expr=(model.CosteII == 400*model.BII+1500*model.yII))
model.ConstII2 = Constraint(expr=(model.CII - 6.5*log(1+model.BII) <=  M*(1-model.yII) ))
model.ConstII3 = Constraint(expr=(model.CII - 6.5*log(1+model.BII) >= -M*(1-model.yII) ))
model.ConstII4 = Constraint(expr=(model.BII <= 40*model.yII))

model.ConstIII1 = Constraint(expr=(model.CosteIII == 550*model.BIII+2000*model.yIII))
model.ConstIII2 = Constraint(expr=(model.CIII - 7.2*log(1+model.BIII) <=  M*(1-model.yIII) ))
model.ConstIII3 = Constraint(expr=(model.CIII - 7.2*log(1+model.BIII) >= -M*(1-model.yIII) ))
model.ConstIII4 = Constraint(expr=(model.BIII <= 40*model.yIII))

model.balance_C = Constraint(expr=(model.CII+model.CIII == model.C))
model.balance_B = Constraint(expr=(model.BI+model.Bext == model.BII+model.BIII))

model.binary = Constraint(expr=(model.yII+model.yIII == 1))
model.upA = Constraint(expr=(model.AI<=16))
model.upC = Constraint(expr=(model.C<=10))

model.Obj = Objective(expr=(1800*model.C-500*model.AI-950*model.Bext-model.CosteI-model.CosteII-model.CosteIII), sense=maximize)
