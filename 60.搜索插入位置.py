# 给定一个排序数组和一个目标值，如果在数组中找到目标值则返回索引。如果没有，返回到它将会被按顺序插入的位置。
# 你可以假设在数组中无重复元素。
# 样例 [1,3,5,6]，5 → 2     [1,3,5,6]，2 → 1     [1,3,5,6]， 7 → 4     [1,3,5,6]，0 → 0
# 挑战 O(log(n)) time
class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if len(A) == 0 or target < A[0]:
            return 0
        if target > A[len(A)-1]:
            return len(A)
        left, right = 0, len(A)-1
        while left <= right:
            mid = (left + right)//2
            if target == A[mid]:
                return mid
            elif target > A[mid]:
                if target < A[mid+1]:
                    return mid+1
                else:
                    left = mid + 1
            else:
                if target > A[mid-1]:
                    return mid
                else:
                    right = mid - 1
if __name__ == '__main__':
    N = int(input('Enter an integer:'))
    a = list()
    for i in range(N):
        a.append(int(input('Enter the data of list:')))
    t = int(input('Enter the target:'))
    s = Solution()
    print(s.searchInsert(a, t))
