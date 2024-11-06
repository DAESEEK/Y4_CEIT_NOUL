def factorial(n):
     if n==0:
          return 1
     return factorial(n-1)*n

print(factorial(5))


def triangle_number(n):
     return triangle_number(n(n+1))
    # write code here 

# Test code : triangle_number(1)부터 triangle_number(10)까지 출력
#for i in range (1, 11):
     print(triangle_number(i))
 
    
#def sum_digits(n):
     if n<10:
          return n
     result_n=sum_digits(n//10)+n%10
     return result_n
    # 여기에 코드를 작성하세요


#print(sum_digits(22541))
#print(sum_digits(92130))
#print(sum_digits(12634))
#print(sum_digits(704))
#print(sum_digits(3755))