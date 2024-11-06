import math

def calculate_sine(angle_in_degrees):
     
     angle_in_radians = math.radians(angle_in_degrees)
     
     sine_value = math.sin(angle_in_radians)
     
     return sine_value
     
def calculate_cosine(angle_in_degrees):
     
     angle_in_radians = math.radians(angle_in_degrees)
     
     cosine_value = math.cos(angle_in_radians)
     
     return cosine_value
     

user_angle=float(input("Enter angle:"))


result1 = calculate_sine(user_angle)
result2 = calculate_cosine(user_angle)

print(f"{user_angle}degree's sine is {result1} and cosine is {result2}")

