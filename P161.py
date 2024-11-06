# Add comma into between number
num = input('input any number:')
if num.isdigit():
     num=num[::-1] # 123456789=>['1','2','3'.....,'9']=>['9','8','7',....'1']
     ret=''
     for i, c in enumerate(num):
          i +=1
          if i !=len(num) and i%3 ==0:
               ret +=(c+',')
          else:
               ret +=c
     ret = ret[::-1]
     print(ret)
else:
     print("input data [%s] It's not number."%num)