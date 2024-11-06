tu=('a','b','c')
print(tu[0])
# tu[2]='d'
a=('a','b','c')
print(a[1])
#a[2]='3'

print('b' in tu)
print(len(a))

#변수할당하기
a1,a2,a3 = a
print(a2)

#리스트에서 튜플로 바꾸기 튜플에서 
print(tuple(a))
print(list(a))

a='hello!'
b='youjun!'
print(a,b)
c=a
a=b
b=c
print(a,b)
(a,b)=(b,a)
print(a,b)
