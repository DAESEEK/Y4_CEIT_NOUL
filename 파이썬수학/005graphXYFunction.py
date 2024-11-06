# x,y 함수 그래프 

import matplotlib.pyplot as plt

# 꺽은선 그래프 line graph 

x = list(range (1,11))
y = []

for i in range(10):
     y.append(3*x[i]-24)  # y=3x-24
     
print(y)
# graph
plt.plot(x,y)
plt.grid(color='0.8')
plt.show()



