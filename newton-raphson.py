import numpy as np

def f(x):
    return x**3 - 4*x - 9  # Example function

def f_derivative(x):
    return 3*x**2 - 4  # Derivative of the function

def newton_raphson(x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        fpx = f_derivative(x)
        if abs(fpx) < 1e-10:
            print("Derivative too small, stopping iteration.")
            return None
        
        x_new = x - fx / fpx
        
        if abs(x_new - x) < tol:
            return x_new
        
        x = x_new
    
    print("Maximum iterations reached without convergence.")
    return None

# Example usage
initial_guess = 2.0
root = newton_raphson(initial_guess)
print(f"Root found: {root}")
