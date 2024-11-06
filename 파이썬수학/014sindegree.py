import math

#degree to radians

def degrees_to_radians(degrees):
     return degrees*math.pi/180

def sine_of_angle(degrees):
     radians= degrees_to_radians(degrees)
     return math.sin(radians)

angle_degree=70
sine_valus=sine_of_angle(angle_degree)

print(f"the sine of {angle_degree} degrees is :{sine_valus}")