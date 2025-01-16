#https://www.youtube.com/watch?v=9A8wEAIZmes for i in nums[:]:

#Non working solution why?
def removeElement(nums, val):
    newlist = []
       
    for i in nums:
        if i != val:
            newlist.append(i)

    nums = newlist       
    return len(nums)

print(f'Len: {removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)}')

#Working solution

class Solution:
    def removeElement(nums, val) -> int:    
        for i in nums[:]:
            if i == val:
                nums.remove(i)
        return len(nums)