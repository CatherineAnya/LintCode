# 题目描述：给出2*n+1个的数字，除其中一个数字之外其他每个数字均出现两次，找到这个数字
# 输入：含有2*n+1个数的数组
# 输出：只出现一次的数
# 样例：[1,2,2,1,3,4,3] --> 4
# 挑战：一次遍历，常数级的额外空间复杂度
############
# 题目分析：一次遍历，第一个元素始终与后面的元素进行比较，相同则移除这两个元素，不同则继续比较
# 考虑一：当数组长度为1，即只有一个元素的时候，返回这个元素
# 考虑二：当比较到最后仍不同的时候，返回第一个元素
############
# 知识点：
# 1. list.pop(index)：Python列表的方法，移除列表中的一个元素(默认最后一个元素)，并返回该元素的值
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        # write your code here
        j = 1
        while len(A):
            if len(A) == 1:
                return A[0]
            if A[0] != A[j]:
                j += 1
                if j == len(A):
                    return A[0]
            else:
                A.pop(0)
                A.pop(j-1)
                j = 1
if __name__ == '__main__':
    N = int(input('Enter an integer:'))
    intArray = list()
    for i in range(2*N+1):
        intArray.append(input('Enter a integer:'))
    s = Solution()
    print(s.singleNumber(intArray))
