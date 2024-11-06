li = []
li = list()

li=['a','b','c']

li[0]
print(li[1])

li=['a','b','c','d','e']
print(li.index('c')) 

li.append('f')
print(li)

li.insert(0,'aa')
print(li)

li.remove('aa')
print(li)
del li[2]
print(li)

print( 'b' in li)