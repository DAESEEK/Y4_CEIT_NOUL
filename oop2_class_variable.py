class User:
    count =0
    def __init__(self, name, email, pw):
        self.neme=name
        self.email=email
        self.pw=pw
        
        User.count +=1
       
print(User.count)      
user1 = User("Young", "young@codeit.kr", "123456")
print(User.count)
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "yoon123")
print(User.count)
user3 = User("Taeho", "taeho@codeit.kr", "223344")
print(User.count)
user4 = User("Lisa", "lisa@codeit.kr", "12345")
print(User.count)


