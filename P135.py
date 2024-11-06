add = lambda x,y:x+y  # def add(x,y):  x+y   ret = add(2,3) . ==> 4
ret = add(1,3)
print(ret)   # 4가 출력됨

funcs =[lambda x:x+'.pptx' ,lambda x:x+'.docx']

ret1 = funcs[0]('intro')
ret2= funcs[1]('Report')

print(ret1) #
print(ret2) #

names ={'Mary':10999, 'Sams': 2111, 'Tom':20245,
 'Micale':27115,'Bob':5887,'Kelly':7855}

ret3 = sorted(names.items(),key=lambda x:x[0])
print(ret3)

