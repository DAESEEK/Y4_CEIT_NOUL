from matplotlib.pyplot import switch_backend
from Add import plus 
from Sub import minus

num1 = int(input('숫자를 입력하세요 :'))
num2 = int(input('숙자를 한번더 입력하세요:'))
cal = str(input('원하는 계산에 따라 기호를 넣으세요 (+,-,/,*):'))

if cal =="+":
     plus(num1,num2)
elif cal=="-":
     minus(num1,num2)