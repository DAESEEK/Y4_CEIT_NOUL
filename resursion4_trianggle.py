def triangle_number(n):
     if n==1:
          return 1
     return triangle_number(n-1)+n

for i in range (1,11):
     print(triangle_number(i))