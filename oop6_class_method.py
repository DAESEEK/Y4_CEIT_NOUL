class User:
     count =0
     
     def __init__(self,name,email,password):
          self.name = name
          self.email = email
          self.password = password
          
          User.count +=1
     
     def say_hello(self):
          print("Hello! I am {}".format(self.name))
     def __str__(self):
          return "Name : {}, E-mail : {}, Password: ******** " .format(self.name,self.email)
     @classmethod
     def number_of_users(cls):  # instance => self class ==> cls 
          print("Total Users: {}".format(cls.count)) # cls.count== User.count //Class method call intance method or class method
     
user1= User("kim","kkk@iater.org","123456")
user2= User("Young","youn@iater.org","654321")
user3= User("Lee","lee@iater.org","1y3uiy7")

User.number_of_users()
