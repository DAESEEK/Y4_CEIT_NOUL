class User:
     def __init__(self, name, email, password):
         self.name=name
         self.email=email
         self.password=password
     
     @classmethod
     def from_string(cls,string_params):
          #cls.param_list=string_params.split(",")
          from_string=string_params.split(",")
          name =from_string[0]
          email=from_string[1]
          password = from_string[2]
          
          return cls(name,email,password)
     @classmethod
     def from_list(cls, list_params):
          #cls.param_list = list_params.split(",")
          from_list=list_params.split(",") 
          name=list_params[0]
          email= list_params[1]
          password = list_params[2]
          
          return cls(name,email,password)
     
youn = User.from_string("Yoon, yoon@iater.org, 123456")
younsoo = User.from_list("UUU, youn@iater.org, 654321")

print(youn.name,youn.email,youn.password)
print(younsoo.name,younsoo.email,younsoo.password)

