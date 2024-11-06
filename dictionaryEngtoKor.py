with open('vocabulary.txt','a') as f:
     
     while True:
          Eng_word = input("Input English word :")
          if Eng_word =="q":
               break
          Kor_word = input("Input Korean word :")  
          f.write (Eng_word + " : " + Kor_word + "\n")
               
                       
               
          