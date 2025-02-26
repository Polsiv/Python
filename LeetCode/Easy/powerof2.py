#https://www.youtube.com/watch?v=ZixRC6stfMg

from math import log
def isPowerOfTwo(n: int) -> bool:
        if isinstance(log(n, 2), float):
            return True
        else: 
            return False
print(isPowerOfTwo(16))