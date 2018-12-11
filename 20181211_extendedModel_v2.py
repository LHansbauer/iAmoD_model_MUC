import numpy as np
import pandas as pd
from gurobipy import*

import inputData2 as id

# Optimierungsmodell
m = Model('amodRequests')


# Add variables
    # flow
flow = m.addVars(id.customer, id.nodes, id.nodes, name='flow')


# Add Objective function
obj = quicksum(
    flow[c,i,j] * id.distancesAsDict[i,j]
    for c in id.customer for i in id.nodes for j in id.nodes
               )

m.setObjective(obj, GRB.MINIMIZE)


# Add Constraints
    # flow conservation
flowCons = m.addConstrs(
        (flow.sum(c, '*', j) + id.originsAsDict[c, j] == flow.sum(c, j, '*') + id.destinationsAsDict[c, j]
        for c in id.customer for j in id.nodes), name="flowCons")

    # road capacity


# Compute optimal solution
m.optimize()


# Print solution
print('Obj: %g' % m.objVal)

for v in m.getVars():
    if v.x ==1:
        print('%s %g' % (v.varName, v.x))