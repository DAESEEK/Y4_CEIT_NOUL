import matplotlib.pyplot as plt 
import numpy as np

#샘플 데이터 생성
x = np.linspace(0,10,100)
y = np.sin(x)

# 선 그래프 생성
plt.plot(x,y)

# 축 범위 설정 : x축은 0부터 10 y 축은 -1.5부터 1.5까지 
plt.axis([0,10,-1.5,1.5])
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# 격자 추가 
plt.grid(True)

# 그래프 제목 설정
plt.title('Sine Wave Example')

# 그래프 표시 
plt.show()

