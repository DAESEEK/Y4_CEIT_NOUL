class SimpleCalculator:
    # calculate method
    @staticmethod
    def add(first_number, second_number):
        return first_number+second_number
        # Adds two parameters and returns them
    
    @staticmethod
    def subtract(first_number, second_number):
        return first_number-second_number
        
        # Returns the value of the first parameter minus the second parameter.
    
    @staticmethod
    def multiply(first_number, second_number):
        return first_number*second_number
        # Returns the product of two numbers received as parameters
    
    @staticmethod
    def divide(first_number, second_number):
        return first_number/second_number
        # Returns the value of the first parameter divided by the second parameter.
    
    
# Create calculator instance
calculator = SimpleCalculator()
    
# calculator operation call
print(calculator.add(4, 5))
print(calculator.subtract(4, 5))
print(calculator.multiply(4, 5))
print(calculator.divide(4, 5))
