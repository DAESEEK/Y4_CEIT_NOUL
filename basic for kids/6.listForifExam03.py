num = int(input('number? '))
li = []
nli=[]
for i in range(0,len(li)):
     a=li[i]
     b=a.startswith("7")
     if b==True:
      b='XX'
      nli.append(b)
     else:
          nli.append(a)
print(nli)
