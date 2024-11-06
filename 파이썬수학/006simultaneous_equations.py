from sympy import Symbol, solve
import matplotlib.pyplot as plt
# 식의 정의 

a = Symbol('a')
b = Symbol('b')

ex1 = a+b-1
ex2 = 5*a+b-3

print(solve((ex1,ex2)))


#x = list(range (1,11))
#y = []

#for i in range(10):
 #    y.append(solve(ex1)*x[i]-solve(ex2))  # y=3x-24
     


# graph
#plt.plot(x,y)
#plt.grid(color='0.8')
#plt.show()