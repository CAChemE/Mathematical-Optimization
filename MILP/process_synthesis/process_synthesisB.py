#Author: [Carlos Planelles](https://github.com/Planelles20)
from __future__ import division
import numpy as np
from pyomo.environ import *

model = ConcreteModel()


model.yI   = Var(within=Binary)
model.yII  = Var(within=Binary)
model.yIII = Var(within=Binary)

model.CosteI   = Var()
model.CosteII  = Var()
model.CosteIII = Var()

model.AI   = Var(domain=NonNegativeReals)

model.Bext   = Var(domain=NonNegativeReals)
model.BI   = Var(domain=NonNegativeReals)
model.BII  = Var(domain=NonNegativeReals)
model.BIII = Var(domain=NonNegativeReals)

model.C    = Var(domain=NonNegativeReals)
model.C1   = Var(domain=NonNegativeReals)
model.C2   = Var(domain=NonNegativeReals)
model.CII  = Var(domain=NonNegativeReals)
model.CIII = Var(domain=NonNegativeReals)

#constraints

model.ConstI1 = Constraint(expr=(model.CosteI == 250*model.AI+1000*model.yI))
model.ContI2 = Constraint(expr=(model.BI == 0.9*model.AI))
model.ContI3 = Constraint(expr=(model.AI <= 40*model.yI))

model.ConstII1 = Constraint(expr=(model.CosteII == 400*model.BII+1500*model.yII))
model.ConstII2 = Constraint(expr=(model.CII == 0.82*model.BII))
model.ConstII3 = Constraint(expr=(model.BII <= 40*model.yII))

model.ConstIII1 = Constraint(expr=(model.CosteIII == 550*model.BIII+2000*model.yIII))
model.ConstIII2 = Constraint(expr=(model.CIII == 0.95*model.BIII))
model.ConstIII3 = Constraint(expr=(model.BIII <= 40*model.yIII))

model.balance_C = Constraint(expr=(model.CII+model.CIII == model.C))
model.balance_B = Constraint(expr=(model.BI+model.Bext == model.BII+model.BIII))

model.binary = Constraint(expr=(model.yII+model.yIII == 1))
model.upA = Constraint(expr=(model.AI<=16))
model.upC = Constraint(expr=(model.C<=15))

model.balance_CC = Constraint(expr=(model.C1+model.C2 == model.C))
model.upC1 = Constraint(expr=(model.C1<=10))
model.upC2 = Constraint(expr=(model.C2<= 5))


model.Obj = Objective(expr=(1800*model.C1+1500*model.C2-500*model.AI-950*model.Bext-model.CosteI-model.CosteII-model.CosteIII), sense=maximize)
