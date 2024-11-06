# 리턴과 프린트 차이

def print_square(x):
     print(x*x)
     
def get_square(x):
     return x*x 

print_square(3)
get_square(3)

print(get_square(3))

print(print_square(3))
