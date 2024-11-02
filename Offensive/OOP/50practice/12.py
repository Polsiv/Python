def log_method(func):
    def wrapper(self, *args, **kwargs):
        print(f"Calling method: {func.__name__}")
        return func(self, *args, **kwargs)
    return wrapper

class Calculator:
    @log_method
    def add(self, a, b):
        return a + b

    @log_method
    def subtract(self, a, b):
        return a - b

    @log_method
    def multiply(self, a, b):
        return a * b

    @log_method
    def divide(self, a, b):
        return a / b
        
calc = Calculator()
print(calc.add(5, 3))
print(calc.subtract(5, 3))
print(calc.multiply(5, 3))
print(calc.divide(5, 3))
