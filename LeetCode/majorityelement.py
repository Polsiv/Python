class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequencies = {}
        count = 0
        for i in :
            frequencies[i] = frequencies.get(i, 0) + 1

        return max(frequencies, key=frequencies.get)


        
