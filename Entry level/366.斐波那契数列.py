# 题目描述：查找斐波纳契数列中的第N个数
# 输入：N
# 输出：对应的斐波那契数
# 样例：1 --> 0，2 --> 1，10 --> 34
############
# 题目分析：
# 1. 斐波那契数列：前2个数是0和1，第i个数是第i-1个数和第i-2个数的和
# 2. 斐波那契数列前10个数是：0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
# 3. 生成的斐波那契数列需要用列表来存储，考察Python列表的使用
############
# 知识点：
# 1. 列表(list)：Python序列的内置数据类型之一，其数据项不需要具有相同的类型
# 2. 定义列表：list1 = list() 或 list2 = []，推荐第一种方式
# 3. list.append()：Python列表的方法，在列表的末尾添加新的数据项，无返回值，直接更新列表
# 4. range(startnum,endnum,step)：Python的内置函数，一个迭代器，返回一系列连续的整数列表，多在for循环中做为索引使用
# 5. len()：Python的内置函数，返回字符串、列表、元组等对象的长度或项目个数
class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        if n <= 0:
            return 0
        f = list()
        f.append(0)
        f.append(1)
        for i in range(n):
            if len(f) < (i+1):
                f.append(f[i-1]+f[i-2])
        return f[n-1]
if __name__ == '__main__':
    s = Solution()
    num = int(input('Enter N:'))
    print(s.fibonacci(num))
