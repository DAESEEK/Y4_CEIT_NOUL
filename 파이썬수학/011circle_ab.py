import matplotlib.pyplot as plt   
import numpy as np   

# center of circle
a = 200
b = 300

# circle function

r=300                             # radious
x = np.arange(a-r,a+r+1)         # x(200,300) center of circle
                                  # radious 300
y = np.sqrt(r**2 - (x-a)**2)+b    # upper circle
y2= -y+2*b

#drawing
plt.plot(x,y)
plt.plot(x,y2)
plt.axis('equal')
plt.grid(color='0.8')
plt.show()

