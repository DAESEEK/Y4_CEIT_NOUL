# 스택에 대한....
mystack= []

def putdata(data):
     global mystack
     mystack.append(data)

def popdata():
     global mystack
     if len(mystack)==0:
          return None
     return mystack.pop()

putdata('Data1')
putdata([3,4,5,6,7,8])
putdata(12345)

print('stack status:',end=''); print(mystack)

ret = popdata()
while ret !=None:
     print('Data extraction :',end=''); print(ret)
     print('Stack status :',end=''); print(mystack)
     ret = popdata()

putdata(1)
putdata('8')
putdata(33)
print('stack status:',end=''); print(mystack)

popdata()
print('Stack status :',end=''); print(mystack)