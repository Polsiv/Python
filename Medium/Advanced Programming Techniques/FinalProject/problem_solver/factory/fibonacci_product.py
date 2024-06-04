from .i_problem_solver import IProblemSolver

class FibonacciProduct(IProblemSolver):

    def compute_results(self, data: list) -> list[str]:
        list_result = []
        for num in data:
            result = self.__fibonacci(int(num))
            list_result.append(str(num) + " " + str(result))
        return list_result

    def __fibonacci(self, data):
        if data < 0:
            return False

        a, b = 0, 1

        if data == b or data == a:
            return True

        while b < data:
            a, b = b, a + b
            if b == data:
                return True
        return False
