#My solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        inverse = []
        normal = []
        for i in range(len(x) -  1, -1, -1):
            inverse += x[i]

        for i in range(len(x)):
            normal += x[i]
        
        if inverse == normal: return True
        else: return False

#better solution
def isPalindrome(x: int) -> bool:
    reverse = ""
    for i in str(x):
        reverse = i + reverse
    
    print(reverse)
    print(str(x))
        
    if reverse == str(x): return True
    else: return False

isPalindrome(522)