# 给定一个排序的整数数组（升序）和一个要查找的整数target，用O(logn)的时间查找到target第一次出现的下标（从0开始），如果target不存在于数组中，返回-1。
# 样例
# 在数组 [1, 2, 3, 3, 4, 5, 10] 中二分查找3，返回2。
# 挑战
# 如果数组中的整数个数超过了2^32，你的算法是否会出错？
# 151ms，普遍时间101ms
class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        left, right = 0, len(nums)-1
        while left <= right:
            middle = (left + right)//2
            if nums[middle] == target:
                if nums[middle] != nums[middle-1]:
                    return middle
                else:
                    right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1
if __name__ == '__main__':
    N = int(input('Enter an integer:'))
    L = list()
    for i in range(N):
        L.append(int(input('Enter the data:')))
    t = int(input('Enter an integer:'))
    s = Solution()
    print(s.binarySearch(L, t))
    

# 百度到这个，也是151ms，但是没搞懂他的逻辑
class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        left, right = 0, len(nums)-1
        while left <= right:
            middle = (left + right)//2
            if nums[middle] >= target:
                right = middle - 1
            else:
                left = middle + 1
        if left < len(nums) and nums[left] == target:
            return left
        return -1
