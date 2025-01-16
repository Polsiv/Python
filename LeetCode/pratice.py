#https://www.youtube.com/watch?v=DEJAZBq0FDA Explanation

def removeDuplicates(nums):
    pointer = 1
    for i in (1, len(nums)):
        if nums[i] != nums [i - 1]:
            nums[pointer] = nums [i]
            print(nums)
            pointer += 1
    return pointer

list = [0, 0, 0, 1, 2, 3, 4, 4, 5, 6, 7, 7]

print(removeDuplicates(list))
