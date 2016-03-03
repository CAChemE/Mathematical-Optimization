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
# Cost
model.c = Param(model.F, within = PositiveReals, doc = 'in $')

# Amount of nutrient
model.a    = Param(model.F, model.N, within = NonNegativeReals)

# Max and Min for each Nutrient
model.Nmin = Param(model.N, within = NonNegativeReals, default = 0.0)
model.Nmax = Param(model.N, within = NonNegativeReals, default = infinity)


# Number of servings
model.x = Var(model.F, within = NonNegativeIntegers)

# Minimize z(cost)
def cost(model):
    return sum(model.c[i]*model.x[i] for i in model.F)
model.cost = Objective(rule=cost)

# LIMITS

#Max
def nutrients_max(model, j):
    value = sum(model.a[i,j]*model.x[i] for i in model.F)
    return value <= model.Nmax[j]
model.nutrient_limit_max = Constraint(model.N, rule=nutrients_max)
#Min
def nutrient_min(model, j):
    value = sum(model.a[i,j]*model.x[i] for i in model.F)
    return model.Nmin[j] <= value 
model.nutrient_limit_min = Constraint(model.N, rule=nutrient_min)

#def pyomo_postprocess(options=None, instance=None, results=None):
#    model.x.display()

