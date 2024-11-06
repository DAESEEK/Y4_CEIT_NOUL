import matplotlib.pyplot as plt
import numpy as np  
# 꺽은선 그래프 line graph 

x = np.arange(-1.0,1.01,0.01)
y = x*x*x-2

# graph
plt.plot(x,y)
plt.grid(color='0.8')
plt.show()
