# Look at the following conditions and complete the static methods 
#               of the SimpleCalculator class, which is a calculator class.
#static method
#     add: Returns the sum of two numbers received as parameters.
#     subtract: Returns the value obtained by subtracting 
#                   the second parameter from the first parameter.
#     multiply: Returns the product of two numbers received as parameters.
#     divide: Returns the value of dividing the first parameter by 
#              the second parameter.

class SimpleCalculator:
    # calculate method
    @staticmethod
    def add(first_number, second_number):
        d# Adds two parameters and returns them   
    @staticmethod
    def subtract(first_number, second_number):
        d# Returns the value of the first parameter minus the second parameter.   
    @staticmethod
    def multiply(first_number, second_number):       
        d# Returns the product of two numbers received as parameters   
    @staticmethod
    def divide(first_number, second_number):      
        d# Returns the value of the first parameter divided by the second parameter.      
# Create calculator instance
calculator = SimpleCalculator()
    
# calculator operation call
print(calculator.add(4, 5))
print(calculator.subtract(4, 5))
print(calculator.multiply(4, 5))
print(calculator.divide(4, 5))