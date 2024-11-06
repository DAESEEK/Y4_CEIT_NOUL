def countWord(filename,word):
     with open(filename,'r') as f:
          text = f.read()
          text = text.lower()
          pos = text.find(word)
          count =0
          while pos !=-1:
               count +=1
               pos=text.find(word,pos+1)
     return count
word = input('Enter the word for counting in the file: ')
word = word.lower()
ret = countWord('mydata.txt',word)
print('[%s]\'s count : %d'%(word,ret))