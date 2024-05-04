from .data_handler import DataHandler
from interfaces.i_problem_solver import IProblemSolver

class MyApp:
    def __init__(self, data_handler_instance: DataHandler, primesinstance: IProblemSolver, fibonacciinstance: IProblemSolver) -> None:
        self.data_handler = data_handler_instance
        self.primesolver = primesinstance
        self.fibonnacisolver = fibonacciinstance
    
    def run(self, num):
        if num == 1:
            data = self.data_handler.read_data("Files/prime.input.txt")
            results = self.primesolver.compute_results(data)
            self.data_handler.save_data("Files/prime.output.txt", results)
        if num == 2:
            pass