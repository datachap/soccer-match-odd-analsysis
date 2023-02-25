from scipy.optimize import linprog

# Define the coefficients of the inequalities
A = [[-0.63, 1.10], [1.10, -3.06]]
b = [0, 0]

# Define the lower and upper bounds of the variables
x_bounds = (50, 150)
y_bounds = (50, 150)

# Use linprog to solve the problem
res = linprog(c=[1, 1], A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds])

# Check if the problem has a feasible solution
if res.success:
    # Print the solution
    print(f"x = {round(res.x[0], 2)}, y = {round(res.x[1], 2)}")
else:
    # Print an error message
    print("The problem has no feasible solution.")