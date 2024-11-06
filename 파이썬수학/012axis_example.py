import matplotlib.pyplot  as plt 

x=[1,2,3,4]
y=[1,4,9,16]

plt.plot(x,y)
plt.axis([0,6,0,20])      # 측범위 설정
plt.xlabel('X Axis')    # x측 레이블 설정
plt.ylabel('Y Axis')    # y축 레이블 설정
plt.show()
