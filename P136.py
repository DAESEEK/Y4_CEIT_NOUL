f= lambda x:x*x
args =[1,2,3,4,5]

ret=map(f,args)

print(list(ret))

f=lambda x,y: x*x+y
X=[1,2,3,4,5]
Y=[10,9,8,7,6]

ret=map(f,X,Y)
print(list(ret))