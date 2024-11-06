t1 = input('which word?')
t2 = input('change to ?')

with open('letter.txt','r') as f:
     with open('letter2.txt','w') as h:
          text = f.read()
          text = text.replace(t1,t2)
          h.write(text)
print('[%s] changed to [%s]' %(t1,t2))
