class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        
info_string = "Kang,younghoon@codeit.kr,123456"
info_list = ["lee", "yoonsoo@codeit.kr", "abcdef"]

# User instance making
parameter_list = info_string.split(",") # split method(,)

# Each variable 
younghoon_name = parameter_list[0]
younghoon_email = parameter_list[1]
younghoon_password = parameter_list[2]

younghoon = User(younghoon_name, younghoon_email, younghoon_password)

# User instance making[2]
yoonsoo_name = info_list[0]
yoonsoo_email = info_list[1]
yoonsoo_password = info_list[2]

yoonsoo = User(yoonsoo_name, yoonsoo_email, yoonsoo_password)

# print
print(younghoon.name, younghoon.email, younghoon.password)
print(yoonsoo.name, yoonsoo.email, yoonsoo.password)

        



