from .i_problem_solver import IProblemSolver

class FizzBuzzProduct(IProblemSolver):

    def compute_results(self, data):
        list_result = []
        for num in data:
            result = self.__fizz_buzz(int(num))
            list_result.append(str(num) + " " + result)
        return list_result

    def __fizz_buzz(self, data: int) -> str:
        competedstring = ""
        competedstring += "Fizz" * int(data % 3 == 0)
        competedstring += "Buzz" * int(data % 5 == 0)
        return competedstring or str(data)
