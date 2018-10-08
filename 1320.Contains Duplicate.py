# Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
# 样例
# Given nums = [1,1], return ture.
# 1105ms，大都是101ms
class Solution:
    """
    @param nums: the given array
    @return: if any value appears at least twice in the array
    """
    def containsDuplicate(self, nums):
        # Write your code here
        i, j = 0, 1
        length = len(nums)
        if length == 0 or length == 1:
            return False
        while i < j:
            if nums[i] == nums[j]:
                return True
            else:
                j += 1
                if j == length:
                    i += 1
                    j = i + 1
                    if i == length-1:
                        return False
