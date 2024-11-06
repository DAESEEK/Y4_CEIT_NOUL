import matplotlib.pyplot as plt   
import numpy as np      

# degree

th = np.arange(0,360)


# circle 

x = np.cos(np.radians(th))
y = np.sin(np.radians(th))


# draw
plt.plot(x,y)
plt.axis('equal')
plt.grid(color='0.8')
plt.show()

