import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def differentiate_and_plot():
    # Define variable and function
    x = sp.Symbol('x')
    
    # Get function input from user
    func_str = input("Enter the function to differentiate (use x as the variable): ")
    func = sp.sympify(func_str)
    
    # Calculate derivative
    derivative = sp.diff(func, x)
    
    print(f"Original function: {func}")
    print(f"Derivative: {derivative}")
    
    # Plot graphs
    x_vals = np.linspace(-10, 10, 1000)
    y_vals = [func.subs(x, val) for val in x_vals]
    y_derivative = [derivative.subs(x, val) for val in x_vals]
    
    plt.figure(figsize=(12, 6))
    plt.plot(x_vals, y_vals, label='Original function')
    plt.plot(x_vals, y_derivative, label='Derivative function')
    plt.title('Function and its Derivative')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.axhline(y=0, color='k', linestyle='--')
    plt.axvline(x=0, color='k', linestyle='--')
    plt.show()

# Run the program
differentiate_and_plot()
