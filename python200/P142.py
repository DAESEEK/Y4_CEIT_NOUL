# file copy
f = open('ii.txt','r')
h = open('ii_copy.txt','w')

data = f.read()
h.write(data)
f.close()
h.close()
