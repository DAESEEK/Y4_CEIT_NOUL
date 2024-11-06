class User:
     count =0
    
     def __init__(self, name, email, pw):
          self.name= name
          self.email=email
          self.pw = pw
          
          User.count +=1
user1 = User("Sam","uop@iater.org","238dyu")
user2 = User("Sophia","sopi@gmail.com","du15776")
user3 = User("Yang","ya@naver.com","gh256776")


User.count=5
user1.count=4

print(User.count)
print(user1.count)
print(user2.count)
print(user3.count)  
