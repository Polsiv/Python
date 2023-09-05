class Solution:
    def containsDuplicate(nums) -> bool:
        
        uniques = set(nums)
        if len(uniques) == len(nums):    
            return False
        else:
            return True