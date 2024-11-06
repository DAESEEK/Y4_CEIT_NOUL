# 1 에서  10000 까지  
# 

a = str(list(range(1,10000))).count('8')# 숫자를 문자로 바꾸기 위함
print(a)

count =0
for i in range(10001):
     if '8' in str(i):
          count +=str(i).count('8') # 해당 숫자에 8의 수를 기존 count에 더하는것이다. 
print(count)

b=str([i for i in range(10001)]).count('8')
print(b)

