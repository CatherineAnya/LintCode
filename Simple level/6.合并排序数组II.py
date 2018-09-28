# 题目描述：合并两个排序的整数数组A和B变成一个新的数组
# 输入：数组A和B
# 输出：新数组
# 样例：A=[1,2,3,4]，B=[2,4,5,6] --> [1,2,2,3,4,4,5,6]
# 挑战：若一个数组很大而另一个数组很小的时如何优化算法
############
# 题目分析：
# 一般算法：使用两个循环来把两个数组的值添加到新的数组中，然后排序新的数组，时间复杂度为O(NlogN)
# 优化算法：因为两个数组都是排好序的，进行归并时只需比较两个数组的元素大小，时间复杂度为O(N)
############
# 知识点：
# 1. list.sort()：Python列表的方法，用于对原列表进行排序，无返回值，直接更新列表，默认使用快速排序的方法
# 2. list.extend()：Python列表的方法，
############
# 一般算法：
class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        # 方法二：
        #for j in B:
            #A.append(j)
        #A.sort()
        #return A
        newArray = list()
        for i in A:
            newArray.append(i)
        for j in B:
            newArray.append(j)
        newArray.sort()
        return newArray
if __name__ == '__main__':
    a = list()
    n1 = int(input('Enter the length of the first list:'))
    for x in range(n1):
        num1 = int(input('Enter the data of the first list:'))
        a.append(num1)
    b = list()
    n2 = int(input('Enter the length of the second list:'))
    for y in range(n2):
        num2 = int(input('Enter the data of the second list:'))
        b.append(num2)
    s = Solution()
    print(s.mergeSortedArray(a, b))
############
# 优化算法：
class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        len1 = len(A)
        len2 = len(B)
        i, j = 0, 0
        C = list()
        while i < len1 and j < len2:
            if A[i] < B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        # 方法二：
        #if i < len1:
            #C.extend(A[i:])
        #if j < len2:
            #C.extend(B[j:])
        while i < len1:
            C.append(A[i])
            i += 1
        while j < len2:
            C.append(B[j])
            j += 1
        return C
if __name__ == '__main__':
    a = list()
    n1 = int(input('Enter the length of the first list:'))
    for x in range(n1):
        num1 = int(input('Enter the data of the first list:'))
        a.append(num1)
    b = list()
    n2 = int(input('Enter the length of the second list:'))
    for y in range(n2):
        num2 = int(input('Enter the data of the second list:'))
        b.append(num2)
    s = Solution()
    print(s.mergeSortedArray(a, b))
