from pyomo.environ import *
infinity = float('inf')

# Creation of a Concrete Model
model = AbstractModel()

#DEFINE SETS
# Products
model.F = Set()
# Nutrients
model.N = Set()

# DEFINE PARAMETERS

# Calories
model.Cal = Param(model.F, within = PositiveReals)

# Cost
model.a    = Param(model.F, model.N, within = NonNegativeReals)

# Max and Min Cost
model.Cmin = Param(model.N, within = NonNegativeReals, default = 0.0)
model.Cmax = Param(model.N, within = NonNegativeReals, default = infinity)

# Number of servings
model.x = Var(model.F, within = NonNegativeIntegers)

# MAXIMIZE z(calories)
def calories(model):
    return sum(model.Cal[i] * model.x[i] for i in model.F)
model.calories = Objective(rule=calories, sense=maximize)


#CONSTRAINS

#Max
def cost_max(model, j):
    value = sum(model.a[i,j] * model.x[i] for i in model.F)
    return value <= model.Cmax[j]
model.cost_limit_max = Constraint(model.N, rule=cost_max)

#Min
def cost_min(model, j):
    value = sum(model.a[i,j] * model.x[i] for i in model.F)
    return model.Cmin[j] <= value 
model.cost_limit_min = Constraint(model.N, rule=cost_min)