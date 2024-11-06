class User:
# set Instance variable
     def __init__(self,name,email,password):
          self.name = name
          self.email= email
          self.password = password
          
          self.following_list =[]
          self.followers_list = []
     def follow(self,another_user): # Follow append
          self.following_list.append(another_user)
          another_user.followers_list(self)
     def num_following(self):# how many people follow //return 
          return len(self.following_list)
     def num_followers(self): # how many people followers //return 
          return len(self.followers_list)
#Create Users
user1 = User("Young","young@code.kr","12345") 
user2=User("kang","udd@iam.com","popkdj")
user3=User("kim","kim100@goemail.net","uoiikldsf")     
#User follow
user1.follow(user2)
user1.follow(user3)
user2.follow(user1)


# display user info & follow/ers
print( user1.name,user1.num_followers(),user1.num_following()  )
          