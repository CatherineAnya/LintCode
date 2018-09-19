# 题目描述：反转一个3位整数
# 输入：3位整数
# 输出：反转的整数
# 样例：123 --> 321，900 --> 9
############
# 题目分析：反转即倒序输出，使用Python中字符串的切片操作，以-1的步长从后向前截取
############
# 知识点：
# 1. input()：Python的内置函数，从控制台接收一个标准输入，返回为string类型
# 2. int()：Python的内置函数，将一个字符串或数字转换为整型
# 3. str()：Python的内置函数，将一个对象表现为字符串类型给用户
# 4. 切片操作：[start:end:step]，从某一字符串或序列中截取某段切片，默认步长为1
class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here
        return int(str(number)[::-1])
if __name__ == '__main__':
    n = input('Enter three bit integers:')
    s = Solution()
    print(s.reverseInteger(n))
