from urllib3 import Retry


text = input('Enter the sentance :')

ret = ''
for i in range(len(text)):
     if i!=len(text)-1:
          ret +=text[i+1]
     else: 
          ret +=text[0]
print(ret)
