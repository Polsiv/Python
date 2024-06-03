from ICreator import ICreator
from FizzBuzzCreator import FizzBuzzCreator
from FibonacciCreator import FibonacciCreator
from PrimeCreator import PrimeCreator

def client_code(creator :ICreator):


    test = [121, 21, 273, 13788, 2, 321, 13]

    return creator.problem_to_solve(test)

print(client_code(PrimeCreator()))