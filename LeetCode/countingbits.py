class Solution(object):
    def countBits(n):
        
        ans = []

        tempans = [[], [], [], []]

        for i in range(0, n + 1):
            i = bin(i).replace("0b", "")
            ans.append(i)
    
    
    countBits(4)

