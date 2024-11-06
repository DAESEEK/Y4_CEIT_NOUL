import math


def calculate_square(number):
     return math.sqrt(number)


number = int(input("enter the number :"))

result = calculate_square(number)

print(f"root {number} : {result}")