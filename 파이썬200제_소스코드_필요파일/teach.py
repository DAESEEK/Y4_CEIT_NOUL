import matplotlib.pyplot as plt
import numpy as np

# angle
th = np.arange(0,360)

# point in the circle
r=5
x=r*np.cos(np.radians(th))+3
y=r*np.sin(np.radians(th))+2


     
#draw
plt.plot(x,y)
plt.axis('equal')
plt.grid('color=0.8')
plt.show()