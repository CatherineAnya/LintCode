# 题目描述：有一个数组和两个索引，交换下标为这两个索引的数字
# 输入：数组，index1，index2
# 输出：交换后的数组
# 样例：[1,2,3,4]，index1=2，index2=3 --> [1,2,4,3]
############
# 题目分析：数组即Python列表，考察列表的索引操作
############
# 知识点：
# 1. 索引操作(一)：通过在方括号中指定数据项所处的位置来访问该数据项
# 2. 索引操作(二)：索引可以使用负数，位置计数将从队列末尾开始
class Solution:
    """
    @param A: An integer array
    @param index1: the first index
    @param index2: the second index
    @return: nothing
    """
    def swapIntegers(self, A, index1, index2):
        # write your code here
        t = A[index1]
        A[index1] = A[index2]
        A[index2] = t
        return A
if __name__ == '__main__':
    array = list()
    N = int(input('Enter the list length:'))
    for i in range(N):
        data = int(input('Enter the list data:'))
        array.append(data)
    index1 = int(input('Enter the first index:'))
    index2 = int(input('Enter the second index:'))
    s = Solution()
    print(s.swapIntegers(array, index1, index2))
