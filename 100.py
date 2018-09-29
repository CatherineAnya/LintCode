# 给定一个排序数组，在原数组中删除重复出现的数字，使得每个元素只出现一次，并且返回新的数组的长度。
# 不要使用额外的数组空间，必须在原地没有额外空间的条件下完成。
# 给出数组A =[1,1,2]，你的函数应该返回长度2，此时A=[1,2]。
# 超时
class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        i, j = 0, 1
        while len(nums):
            if len(nums) == 1:
                return len(nums)
            if j == len(nums):
                i += 1
                j = i + 1
                if i >= len(nums) - 1:
                    return len(nums)
            if nums[i] != nums[j]:
                j += 1
            else:
                nums.pop(j)
