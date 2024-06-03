from typing import List
from .Iproblem import IProblemSolver

class Prime(IProblemSolver):

  def compute_results(self, data: List[str]) -> List[str]:
    result = []
    line = ""
    for element in data:
      line = self.__prime_classifier(int(element))
      result.append(element + " " + str(line))
    return result

  def __prime(self,n):
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