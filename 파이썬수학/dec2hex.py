# 이 프로그램은 십진수를 16진수로변환하는 프로그램입니다. 
# cal.py 에서 십진수를 넣으면 됩니다. 

def dec2hex(target):
     reminder =[] # 나머지를 넣는 리스트
     
     # 나머지의 몫이 0이 될때 까지
     while target !=0:
          reminder.append(target%16) #나머지
          target = target//16 # 몫
          
     #나머지 10-15를 A~F로 변환한다. 
     
     
     for i in range (len(reminder)):
          if reminder[i]==10: reminder[i] ='A'
          elif reminder[i]==11: reminder[i]='B'
          elif reminder[i]==12: reminder[i]='C'
          elif reminder[i]==13: reminder[i]='D'
          elif reminder[i]==14: reminder[i]='E'
          elif reminder[i]==15: reminder[i]='F'
     
     #리스트에 있는 요소를 역순으로 한다.
     
     reminder.reverse()
     return reminder
 
print(dec2hex(15))
print(int('0b11010',2))
print(int('0x11',16))
print(hex(16))
print(bin(8))
 
 
          