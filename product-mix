from scipy.optimize import linprog

# Product Mix (simplified model)

# |---------|------|------|------|------|------|------|-------|
# |         | Pr-1 | Pr-2 | Pr-3 | Pr-4 | Pr-5 | Pr-6 | Limit |
# |---------|------|------|------|------|------|------|-------|
# | Revenue |   5  |   6  |   7  |   5  |   6  |   7  |       |
# |---------|------|------|------|------|------|------|-------|
# | Machine |      |      |      |      |      |      |       |
# |  hour   |   2  |   3  |   2  |   1  |   1  |   3  | 1050  |
# |---------|------|------|------|------|------|------|-------|
# | Labour  |      |      |      |      |      |      |       |
# |  hour   |   2  |   1  |   3  |   1  |   3  |   2  | 1050  |
# |---------|------|------|------|------|------|------|-------|
# | Energy  |   1  |   2  |   1  |   4  |   1  |   2  | 1080  |
# |---------|------|------|------|------|------|------|-------|

# The decision variables are the unknown quantities of the products. They are denoted by x1, . . . , x6.
# The revenue to be maximized is:
#                                       5x1 + 6x2 + 7x3 + 5x4 + 6x5 + 7x6
# The resource constraints are:
#                                       2x1 + 3x2 + 2x3 + 1x4 + 1x5 + 3x6 ≤ 1050
#                                       2x1 + 1x2 + 3x3 + 1x4 + 3x5 + 2x6 ≤ 1050
#                                       1x1 + 2x2 + 1x3 + 4x4 + 1x5 + 2x6 ≤ 1080

# Since production must be nonnegative, we impose xj ≥ 0, j = 1, . . . , 6.

# This is a simple LP problem that can be solved by the simplex method.
# The solution is x2 = 240, x4 = 90, x5 = 240, and x1 = x3 = x6 = 0, giving a revenue of 3330.00 units.

# Célfüggvény együtthatói - Objective function coefficients
# Since this is a maximization problem, we can turn it into a minimization problem by multiplying it by -1

# While the problem is simple its analysis highlights some interesting points.
# 1. The most rewarding products (Prod-3 and Prod-6) are not included in the optimal mix.
# 2. It is sufficient to produce not more than three products in order to achieve the maximum possible revenue.
# 3. All resources are fully utilized (constraints are satisfied with equality).

def solve_linear_program():
    # Objective function coefficients (Maximization problem, so we negate it)
    c = [-5, -6, -7, -5, -6, -7]  # -f(x) turns max into min!

    # Left-hand side of the inequality constraints
    A = [
        [2, 3, 2, 1, 1, 3],  # Machine hours constraint
        [2, 1, 3, 1, 3, 2],  # Labor hours constraint
        [1, 2, 1, 4, 1, 2]   # Energy constraint
    ]

    # Right-hand side of the inequality constraints (the limits for resources)
    b = [1050, 1050, 1080]

    # Bounds for the decision variables (non-negative constraints: x1, ..., x6 >= 0)
    bounds = [(0, None)] * len(c)

    # Solving the Linear Programming problem using the simplex method
    result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    # Checking if the optimization was successful and displaying the result
    if result.success:
        print("Optimal solution found!")
        print("Decision variable values (x1, x2, ..., x6):", result.x)
        print("Maximum revenue:", -result.fun)  # Negate the result because we minimized
    else:
        print("Optimization failed:", result.message)

# Main function to run the program

# The optimal solution found by the simplex method is:
# x1 -> 0
# x2 -> 240
# x3 -> 0
# x4 -> 90
# x5 -> 240
# x6 -> 0
# This means that the optimal production mix includes 240 units of Product 2, 90 units of Product 4, and 240 units of
# Product 5, while the other products should not be produced.
# The maximum revenue is 3330.0 units, which is calculated by:
# Revenue: 5x1 + 6x2 + 7x3 + 5x4 + 6x5 + 7x6 = 5 x 0 + 6 x 240 + 7  x 0 + 5 x 90 + 6 x 240 + 7 x 0 = 3300

def main():
    solve_linear_program()

# This ensures that the script runs only when executed directly, not when imported
if __name__ == "__main__":
    main()
