
# return 이 어떻게 하는지... 함수가 어떤 값을 돌려 주는것
# 함수를즉시 종료

def square(x):
     print("start")
     return x*x 
     print("end")    # Dead code

print(square(3))
print("Hello world")


