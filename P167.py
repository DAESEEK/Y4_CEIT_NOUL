with open('letter.txt','r') as f:
     data = f.read()
     tmp = data.split()
     print('words count :[%d]' %len(tmp))