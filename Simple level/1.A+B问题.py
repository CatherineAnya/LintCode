# 题目描述：给出两个32位整数a和b，求他们的和
# 输入：整数a，整数b
# 输出：a+b的和
# 样例：a=1，b=2 --> 3
# 挑战：不使用加减等算数运算符，使用位运算符
############
# 题目分析：考察算数运算符、位运算符的使用
############
# 知识点：
# 1. 
# 2. 
############
# 使用算术运算符
class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        # write your code here
        # return a-(-b)
        return a+b
if __name__ == '__main__':
    A = int(input('Enter an integer:'))
    B = int(input('Enter another integer:'))
    s = Solution()
    print(s.aplusb(A, B))
############
# 使用位运算符
