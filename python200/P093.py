url= 'https://www.google.com/news/today '
log = 'name:konjan age:17 sex:male nation:Lao'

ret1=url.split('/')
print(ret1)

ret2=log.split()
for data in ret2:
     d1,d2 =data.split(':')
     print('%s->%s'%(d1,d2))