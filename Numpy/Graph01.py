
 
import matplotlib.pyplot as plt

#Data
x=[1,2,3,4,5,6,7]
y=[64.3,63.8,63.6,64.0,63.5,63.2,63.1]


#Draw Graph

plt.plot(x,y,color='red',marker='o') # 꺽은선 그래프
plt.grid(False) #격자
plt.show() #화면에 표시
