# Given an array, rotate the array to the right by k steps, where k is non-negative.

# 样例
# Example 1:
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# 注意事项
# 1.Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# 2.Could you do it in-place with O(1) extra space?

# 151ms，还有101ms
# 为什么当 nums = [] 时，输出 [] 是 WA 呢？
# 但是提交为 AC

class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: rotate the array to the right by k steps
    """
    def rotate(self, nums, k):
        # Write your code here
        length = len(nums)
        if length == 0:
            return nums
        k = k % length
        if k == length or k == 0:
            return nums
        diff = length - k
        nums[:] = nums[-k:] + nums[:diff]
        return nums
