from re import A
s= [1,3,4,8,13,17,19,22]
m =max(s)
print(m)
index =0
for i in range(len(s)-1):
     if m> s[i+1] -s[i]:
          index =i
          m = s[i+1]-s[i]
          print(m)
a=[s[index],s[index+1]]
print(a)

s= [1,3,4,8,13,17,20]
ss= [3,4,8,13,17,20]
b= list(zip(s,ss))
print(b)

s=[1,3,4,8,13,17,20]
ss=[4,8,3,13,17,20]

c= sorted(list(zip(s,ss)),key=lambda i:i[1])
print(c)

