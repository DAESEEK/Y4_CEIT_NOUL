import matplotlib.pyplot as plt     
import numpy as np 

# 기본이 되는 선분의 기울기 ອຽງ

a1 = (5-1)/(6-0)
b1 = 1

# 선분의 중점 ຈຸດກາງ
cx = (0+6)/2
cy = (1+5)/2

#선분에 직교하는 직선의 기울기 (a2=-1/a1)
a2= -1/a1

#선분에 직교하는 직선의 절편(b2=y-a2*x)
b2=cy-a2*cx

#직선의 식
x= np.arrange(0,7)
y1=a1*x+b1 #기본직선
y2=a2*x+b2 #
