from .i_problem_solver import IProblemSolver

class PrimeProduct(IProblemSolver):

    def compute_results(self, data: list) -> list[str]:
        list_result = []
        for num in data:
            result = self.__prime_classifier(int(num))
            list_result.append(str(num) + " " + result)

        return list_result

    def __prime(self, data: int) -> str:
        if data <= 1:
            return False
        if data <= 3:
            return True
        if data % 2 == 0 or data % 3 == 0:
            return False
        i = 5
        while i * i <= data:
            if data % i == 0 or data % (i + 2) == 0:
                return False
            i += 6
        return True

    def __prime_classifier(self, data: int) -> str:
        if self.__prime(data):
            return "prime"

        prime_divisors = []
        for i in range(2, data):
            if data % i == 0 and self.__prime(i):
                prime_divisors.append(i)
                if len(prime_divisors) > 2:
                    break

        if len(prime_divisors) == 2:
            if prime_divisors[0] * prime_divisors[1] == data:
                return "semiprime"
        elif len(prime_divisors) == 1:
            if prime_divisors[0] ** 2 == data:
                return "quadratic-semiprime"

        return "no classified"
