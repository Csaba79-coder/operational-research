from scipy.optimize import linprog

# min function
# Z=50x + 20x2 + 30x3 + 80x4
# constraints
# 400x1 + 200x2 + 150x3 + 500x4 ≥ 500
# 3𝑥1 + 2𝑥2 ≥ 6
# 2x1 + 2x2 + 4x3 + 4x4 ≥ 10
# 2x1 + 4x2 + x3 + 5x4 ≥ 8

# it can solve only neg. ...
# -400x1 - 200x2 - 150x3 - 500x4 ≤ -500
# -3𝑥1 - 2𝑥2 ≤ -6
# -2x1 - 2x2 - 4x3 - 4x4 ≤ -10
# -2x1 - 4x2 - x3 - 5x4 ≤ -8

def solve_minimization_problem():
    # Coefficients of the objective function (Z = 50x1 + 20x2 + 30x3 + 80x4)
    c = [50, 20, 30, 80]

    # Coefficients for the inequality constraints (Ax <= b)
    # Converting constraints to <= form
    A = [
        [-400, -200, -150, -500],  # Constraint 1: 400x1 + 200x2 + 150x3 + 500x4 >= 500
        [-3, -2, 0, 0],            # Constraint 2: 3x1 + 2x2 >= 6
        [-2, -2, -4, -4],          # Constraint 3: 2x1 + 2x2 + 4x3 + 4x4 >= 10
        [-2, -4, -1, -5]           # Constraint 4: 2x1 + 4x2 + x3 + 5x4 >= 8
    ]

    # Right-hand side of inequality constraints (converted to <= form)
    b = [-500, -6, -10, -8]

    # Bounds for the variables (x1, x2, x3, x4 >= 0)
    x_bounds = [(0, None), (0, None), (0, None), (0, None)]

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')

    # Return the result
    return res

if __name__ == "__main__":
    result = solve_minimization_problem()

    # Check if the optimization was successful
    if result.success:
        print(f"Optimal values for x1, x2, x3, x4: {result.x}") # x1 = 0, x2 = 3, x3 = 1, x4 = 0
        print(f"Minimum value of Z: {result.fun}") # Z = 90
    else:
        print("Optimization failed:", result.message)
