from ICreator import ICreator
from FizzBuzzCreator import FizzBuzzCreator

def client_code(creator :ICreator):

    test = [12, 21, 273, 13788, 2, 321, 13]

    return (creator.problem_to_solve(test))

client_code(FizzBuzzCreator())