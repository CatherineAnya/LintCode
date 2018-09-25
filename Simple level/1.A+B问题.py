# 题目描述：给出两个32位整数a和b，求他们的和
# 输入：整数a，整数b
# 输出：a+b的和
# 样例：a=1，b=2 --> 3
# 挑战：不使用加减等算数运算符，使用位运算符
############
# 题目分析：考察算数运算符、位运算符的使用
# 1. 首先考虑如何使用位运算符进行两数相加的操作，即a+b=a^b+(a&b)<<1，循环计算，直到(a&b)<<1为0时，返回结果
# 2. 其次考虑两个数同为正、同为负、一正一负、以及一正一负且绝对值相同的时候，是否会出现问题
############
# 知识点：
# 1. 算术运算符：+ 加、- 减、* 乘或者重复若干次字符串、/ 除、% 取余、** x的y次幂、// 整除取整
# 2. 位运算符：把数字看作二进制来进行计算
# 3. &：按位与，两个相应位都为1时才为1，否则为0
# 4. |：按位或，两个相应位有一个为1时结果就为1
# 5. ^：按位异或，相同为0，不同为1
# 6. ~：按位取反，把1变为0，把0变为1
# 7. <<：左移，高位丢弃，低位补0
# 8. >>：右移，高位补0，低位丢弃
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
class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b 
    """
    def aplusb(self, a, b):
        # write your code here
        if a == -b:
            return 0
        while b:
            a, b = a ^ b, (a & b) << 1
        return a
if __name__ == '__main__':
    A = int(input('Enter the first operand:'))
    B = int(input('Enter the second operand:'))
    s = Solution()
    print(s.aplusb(A, B))
