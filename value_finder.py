from scipy.optimize import linprog

# Define the coefficients of the inequalities
def points2invest(odds_low, odds_high, markup_value):
    A = [[-(odds_low-markup_value), markup_value], [markup_value, -(odds_high-markup_value)]]
    B = [0, 0]

    # Define the lower and upper bounds of the variables
    x_bounds = (100, 300)
    y_bounds = (100, 300)

    # Use linprog to solve the problem
    res = linprog(c=[1, 1], A_ub=A, b_ub=B, bounds=[x_bounds, y_bounds])

    # Check if the problem has a feasible solution
    if res.success:
        # Print the solution
        return [round(res.x[0], 2), round(res.x[1], 2)]
        #print(f"x = {round(res.x[0], 2)}, y = {round(res.x[1], 2)}")
    else:
        # Print an error message
        return [0,0]
        #print("The problem has no feasible solution.")