
def add_print_to(original):
     def wrapper():
          print('start function')
          original()
          print('end function')
     return wrapper

@add_print_to
def print_hello():
    print("hello")
    
# print_hello=add_print_to(print_hello)
print_hello()



    
