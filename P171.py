from urllib.request import urlopen

url='http://lkclaos.org/department-of-korean-language/'

#with urlopen(url) as f:
 #    doc = f.read().decode() # byte stream ==> text
  #   with open('lck.html','w') as h:
   #       h.writelines(doc)

with urlopen(url) as f:
     doc = f.read()
     with open('L.html','wb') as h:
          h.write(doc)
