names={'Mary':10999,'Sams':2111,'Aimy':9778,'Tom':20245,
     'Michale':27115,'Bob':5887,'Kelly':7855}
ks = names.keys()
print(ks)

for k in ks:
     print('Key:%s \t Value : %d' %(k,names[k]))

vals= names.values()
print(vals)
vals_list=list(vals)
ret =sum(vals_list)
print(ret)

items=names.items()
print(items)

for item in items:
     print(item)

k = input('Enter name:')
if k in names :
     print ( '%s babies are %d.' %(k, names[k]))
else:
     print('Not exist.')

