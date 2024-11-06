import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return x**2 - 4*x + 4

def f2(x):
    return np.sin(x)

x = np.linspace(-5, 5, 100)
y1 = f1(x)
y2 = f2(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='f1(x) = x^2 - 4x + 4')
plt.plot(x, y2, label='f2(x) = sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('두 함수의 그래프')
plt.legend()
plt.grid(True)
plt.show()