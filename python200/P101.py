#index
solarsys =['Sun','Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Earth']
planet='Earth'
pos=solarsys.index(planet)

print('%s is the %d from Sun' %(planet,pos))
pos=solarsys.index(planet,5)
print('%s is the %d from Sun' %(planet,pos))

planet='Mars'
pos=solarsys.index(planet)
solarsys[pos]='MMars'
print(solarsys)