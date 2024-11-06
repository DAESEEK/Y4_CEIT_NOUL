from poplib import POP3_SSL_PORT


count = 1
data=[]
print('Just enter without any writing')
while True:
     text = input('[%d] write something that save on a file' %count)
     if text == '':
          break
     data.append(text+'\n')
     count +=1
f = open('iidata.txt','w')
f.writelines(data)
f.close()





