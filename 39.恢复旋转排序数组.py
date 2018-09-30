# 给定一个旋转排序数组，在原地恢复其排序。

# 样例
# [4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]

# 挑战
# 使用O(1)的额外空间和O(n)时间复杂度

class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        return nums.sort()
