import matplotlib.pyplot as plt    
import numpy as np

# data

x=np.arange(-1.0,1.0,0.01)
y=3*x**3+2*x**2+2

print (x)
#print(y)
#draw graph

plt.plot(x,y)
plt.grid(color='0.8')
plt.show()

