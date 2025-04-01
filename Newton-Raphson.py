def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """
    Solves f(x) = 0 using the Newton-Raphson method.
    
    Parameters:
    f: function - The function for which we are finding the root.
    df: function - The derivative of the function.
    x0: float - Initial guess.
    tol: float - Tolerance for convergence.
    max_iter: int - Maximum number of iterations.
    
    Returns:
    float - Approximate root of f(x).
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        
        if abs(dfx) < 1e-12:  # Avoid division by zero
            raise ValueError("Derivative too close to zero, try another initial guess.")
        
        x_new = x - fx / dfx
        
        if abs(x_new - x) < tol:  # Check for convergence
            return x_new
        
        x = x_new
    
    raise ValueError("Maximum iterations reached without convergence.")

# Example usage:
import math

# Define function and its derivative
def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

# Initial guess
x0 = 1.5

# Solve for root
root = newton_raphson(f, df, x0)
print(f"Root: {root}")
