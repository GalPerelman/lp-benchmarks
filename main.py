import gurobipy as gp
from gurobipy import GRB



model = gp.read("mps/qap15.mps")

# Solve
model.Params.LogToConsole = 0
model.optimize()
print(model.status, f"{model.Runtime:.3f}", model.ObjVal)

