import cvxpy as cp
import numpy as np

T = 24

p = np.array([
    5, 4, 3, 2, 2, 3,
    4, 6, 8, 10, 9, 7,
    6, 5, 4, 3, 2, 3,
    5, 7, 9, 8, 6, 5
])

d = np.array([
    4, 5, 4, 3, 3, 4,
    6, 8, 10, 9, 8, 7,
    6, 5, 5, 6, 7, 8,
    10, 11, 9, 8, 6, 5
])

B = 20

x = cp.Variable(T, nonneg=True)
s = cp.Variable(T, nonneg=True)

objective = cp.Minimize(p @ x)
constraints = []

for t in range(T):
    if t == 0:
        s_prev = 0
    else:
        s_prev = s[t-1]

    constraints.append(s[t] == s_prev + x[t] - d[t])

    constraints.append(x[t] >= d[t] - s_prev)

    constraints.append(s[t] <= B)


problem = cp.Problem(objective, constraints)
problem.solve()


print("Optimal cost:", problem.value)
print("Optimal purchases x*:", x.value)
print("Storage levels s*:", s.value)