class User:
      
 def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = password
   
    self.following_list = []  
    self.followers_list = [] 
 def __str__(self):
     return "user:{}, e-mail:{}, password:*****".format(self.name,self.email)
 
 def follow(self, another_user):
  self.following_list.append(another_user)
  another_user.followers_list.append(self)

 def num_following(self):
  return len(self.following_list)
  
 def num_followers(self):
  return len(self.followers_list)

user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "yoon123")
user3 = User("Taeho", "taeho@codeit.kr", "223344")
user4 = User("Lisa", "lisa@codeit.kr", "12345")

user1.follow(user2)
user1.follow(user3)
user2.follow(user1)
user2.follow(user3)
user2.follow(user4)
user4.follow(user1)

#print(user1.name, user1.num_followers(), user1.num_following())
#print(user2.name, user2.num_followers(), user2.num_following())
#print(user3.name, user3.num_followers(), user3.num_following())
#print(user4.name, user4.num_followers(), user4.num_following())

print(user1)
print(user2)
print(user3)
print(user4)