# pylint: skip-file
from factory import fibonacci_creator, fizzbuzz_creator, prime_creator
import pytest

@pytest.fixture
def fibonacci():
    return get_problem_creator("FibonacciVerifier")

@pytest.fixture
def fizzBuzz():
    return get_problem_creator("FizzBuzz")

@pytest.fixture
def prime():
    return get_problem_creator("PrimeClassifier")

def get_problem_creator(problem):
    if problem == "FizzBuzz":
        return fizzbuzz_creator.FizzBuzzCreator()
    elif problem == "PrimeClassifier":
        return prime_creator.PrimeCreator()
    elif problem == "FibonacciVerifier":
        return fibonacci_creator.FibonacciCreator()

def test_solve_problems(fizzBuzz, fibonacci, prime):
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = fizzBuzz.problem_to_solve(data)
    assert result == ["1 1", "2 2", "3 Fizz", 
                      "4 4", "5 Buzz", "6 Fizz", "7 7", "8 8", "9 Fizz", "10 Buzz"]

    result = fibonacci.problem_to_solve(data)
    assert result == ["1 True", "2 True", "3 True", "4 False", 
                      "5 True", "6 False", "7 False", "8 True", "9 False", "10 False"]

    result = prime.problem_to_solve(data)
    assert result == ["1 no classified", "2 prime", "3 prime", "4 quadratic-semiprime",
                       "5 prime", "6 semiprime", "7 prime", "8 no classified", "9 quadratic-semiprime", "10 semiprime"]

