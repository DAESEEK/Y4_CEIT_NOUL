import random
num= int(input("1-20 쳐보세요:"))
a= 5 #random.randint(1,20)

for i in range(1,4):
     if a == num:
          print("축하합니다",i,"만에 맞히셨습니다.")
     elif a>num:
          print("기회가",(4-i),"남았습니다.")
          print("UP")
          num=int(input("1-20사이의 숫자를 맞혀보세요:"))
     else: 
          print("기회가",(4-i),"남았습니다")
          print("Down")
          num=int(input("1-20사이의 숫자를 맞혀보세요:")) 
     

