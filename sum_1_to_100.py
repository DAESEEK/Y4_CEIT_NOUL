import matplotlib.pyplot as plt
import numpy as np

# 함수 정의
def y(x):
    return 2*x + 3

# x 값 배열 생성
x_values = [1, 2, 3, 4, 5]

# y 값 계산
y_values = [y(x) for x in x_values]

# 결과 출력
print("x 값:", x_values)
print("y 값:", y_values)

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, 'ro-', label='y = 2x + 3')  # 빨간 점과 선으로 표시
plt.plot(np.linspace(0, 6, 100), y(np.linspace(0, 6, 100)), 'b--', label='연속 함수')  # 파란 점선으로 연속 함수 표시

plt.title('y = 2x + 3 그래프')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.axis([0, 6, 0, 15])  # x축과 y축의 범위 설정

plt.show()
