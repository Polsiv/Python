from problem_solver.factory.i_problem_creator import ICreator
from problem_solver.factory.fizzbuzz_creator import FizzBuzzCreator
from problem_solver.factory.fibonacci_creator import FibonacciCreator
from problem_solver.factory.prime_creator import PrimeCreator

def client_code(creator :ICreator):


    test = [121, 21, 273, 13788, 2, 321, 13]

    return creator.problem_to_solve(test)

print(client_code(PrimeCreator()))