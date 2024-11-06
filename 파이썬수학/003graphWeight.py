# 이프로그램은 일주일간의 체중변화를 그래프로 그리기위하여 matplotlib를 사용했습니다. 

import matplotlib.pyplot as plt 

# data

x=[1,2,3,4,5,6,7]
y=[64.3,63.8,63.6,64.0,63.5,63.2,63.1]

# drew graph

plt.plot(x,y, marker='o')     #꺽은선 그래프 막대그래프(plt.bar(x,y) 원그래프 plt.pie()
plt.grid(color='0.8') # 격자를 표시  
plt.show()    # 화면에 표시   
