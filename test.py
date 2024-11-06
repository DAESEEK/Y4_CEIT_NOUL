import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, exp, lambdify

# Define variable x
x = symbols('x')

# Define function
f = x**2 + 2*x + exp(x)

# Differentiate function f with respect to x
df = diff(f, x)

# Convert sympy expressions to numpy functions
f_np = lambdify(x, f, 'numpy')
df_np = lambdify(x, df, 'numpy')

# Create x values
x_vals = np.linspace(-2, 5, 100)

# Calculate y values for original function and its derivative
y_vals = f_np(x_vals)
dy_vals = df_np(x_vals)

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(x_vals, y_vals, label='Original function')
plt.plot(x_vals, dy_vals, label='Derivative')
plt.axhline(y=0, color='k', linestyle='--')
plt.axvline(x=0, color='k', linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Original Function and its Derivative')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

# Print function expressions
print(f"Original function: {f}")
print(f"Differentiated function: {df}")

# Calculate derivative values for x from 0 to 5
print("\nDerivative values for x from 0 to 5:")
for i in range(6):
    value = df.subs(x, i).evalf()
    print(f"x = {i}: {value}")