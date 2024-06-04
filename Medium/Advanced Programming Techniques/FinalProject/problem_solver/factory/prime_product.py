from .i_problem_solver import IProblemSolver

class PrimeProduct(IProblemSolver):

  def compute_results(self, data: list) -> list[str]:
    list_result = []
    for num in data:
      result = self.__prime_classifier(int(num))
      list_result.append(str(num) + " " + result)
    return list_result

  def __prime(self, n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

  def __prime_classifier(self,n):
    if self.__prime(n):
        return "prime"

    prime_divisors = []
    for i in range(2, n):
        if n % i == 0 and self.__prime(i):
            prime_divisors.append(i)
            if len(prime_divisors) > 2:
                break

    if len(prime_divisors) == 2:
        if prime_divisors[0] * prime_divisors[1] == n:
            return "semiprime"
    elif len(prime_divisors) == 1:
        if prime_divisors[0] ** 2 == n:
            return "cuadratic-semiprime"

    return "No classified"
