# 题目描述：给一组整数，按照升序排序，使用选择排序，冒泡排序，插入排序或者任何O(n^2)的排序算法
# 输入：排序前的整数数组
# 输出：排序后的整数数组
# 样例：[3,2,1,4,5] --> [1,2,3,4,5]
############
# 题目分析：考察Python排序算法，了解各个排序算法的概念，核心就是两两比较
############
# 知识点：
# 1. 
# 2. 
class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        # write your code here
        A.sort()
