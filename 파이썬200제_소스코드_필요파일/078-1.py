txt = 'abcdefghijk'
ret = ''
for i in range(len(txt)):
   ret += txt[-(i+1)]
print(ret)
