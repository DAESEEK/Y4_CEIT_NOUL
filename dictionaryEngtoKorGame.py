with open ('vocabulary.txt', 'r',encoding='UTF-8') as f:
     
     for line in f :
          data = line.split(" : ")
          
          eng_word,kor_word = data[0],data[1]          
          quiz = input(f"{kor_word}: ")
               
          if quiz== eng_word:
               print("You are correct!!")
          else:
               print (f"Sorry. There is {eng_word} ")
