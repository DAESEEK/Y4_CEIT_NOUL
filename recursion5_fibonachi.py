def fib(n):
     if n==0 or n==1:
          return 1
     return fib(n-1)+fib(n-2)

for i in range(1,11):
     print(fib(i))