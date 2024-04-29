from Interfaces.i_problem_solver import IProblemSolver

class FizzBuzz(IProblemSolver):
    
    def __init__(self) -> None:
        pass

    def compute_result(self, data):
        competedstring = ""
        competedstring += "Fizz" * int(data % 3 == 0)
        competedstring += "Buzz" * int(data % 5 == 0)
        return competedstring or str(data)