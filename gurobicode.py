from gurobipy import *

# try:

# Create a new model
model = Model("mip1")
m = 5
n = 11

M = [
    [375, 12, 142, 245, 412],
    [632, 452, 758, 278, 398],
    [12, 876, 124, 534, 765],
    [460, 542, 523, 120, 499],
    [528, 101, 789, 124, 999],
    [796, 245, 632, 375, 123],
    [532, 230, 543, 896, 452],
    [14, 124, 214, 543, 785],
    [257, 527, 753, 210, 463],
    [896, 896, 214, 258, 259],
    [532, 302, 501, 765, 988]
]

# Create variables
# orders = model.addVars( n, lb = 1, ub = 11 , vtype = GRB.INTEGER )

orders = model.addVars(n, n, lb=0, ub=1, vtype=GRB.BINARY)
order = model.addVars(n, lb=0, ub=n-1, vtype=GRB.INTEGER)

startime = model.addVars(n, m, lb=0, vtype=GRB.INTEGER)
endtime = model.addVars(n, m, lb=0, vtype=GRB.INTEGER)
Makespan = model.addVar(lb=0, vtype=GRB.INTEGER)

# orderss = []
# for i in range(n):
#     orders = []
#     for j in range(n):
#         orders.append( model.addVar( lb = 0, ub = 1 , vtype = GRB.BINARY, name = "range {} {}".format(i,j) ) )
#     orderss.append(orders)

model.addConstrs(orders.sum(i, '*') == 1 for i in range(n))
model.addConstrs(orders.sum('*', i) == 1 for i in range(n))
for i in range(n):
    model.addConstr(order[i] == (
        quicksum(j * orders[i, j] for j in range(n))))

for i in range(n):
    for j in range(m):
        # print(i,j)
        model.addConstr( endtime[i,j] - startime[i,j] == M[i][j])

for k in range(m):
    for i1 in range(n):
        for i2 in range(n):
            for j in range(1,n-1):
                model.addConstr( 
                    
                    (startime[i1,k] - endtime[i2,k]) * ( orders[i1,j] * orders[i2,j-1] ) >= 0 
                    
                    )
        
model.addConstr( Makespan == max_( (( endtime[ j, i ]  for i in range(m) for j in range(n) )  ) ))

x = model.addVar(vtype=GRB.BINARY, name="x")
y = model.addVar(vtype=GRB.BINARY, name="y")
z = model.addVar(vtype=GRB.BINARY, name="z")

# Set objective
# model.setObjective(x + y + 2 * z, GRB.MAXIMIZE)

# Add constraint: x + 2 y + 3 z <= 4
model.addConstr(x + 2 * y + 3 * z <= 4, "c0")

# Add constraint: x + y >= 1
model.addConstr(x + y >= 1, "c1")

model.setObjective(Makespan, GRB.MINIMIZE)

# for v in model.getVars():
#     print(v.varName, v.x)
model.optimize()

for i in range(n):
    for j in range(n):
        print(int(orders[i, j].x), end=' ')
    print("")

for i in range(n):
    print(int(order[i].x), end=' ')
print('Obj:', model.objVal)

print("start time")
for i in range(n):
    for j in range(m):
        print(int(startime[i, j].x), end=' ')
    print("")

print('end time')
for i in range(n):
    for j in range(m):
        print(int(endtime[i, j].x), end=' ')
    print("")

# except GurobiError:
#     print('Error reported')
