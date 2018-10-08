# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# 样例
# Example1:
# Given num = 16, 
# return true.

# Example2:
# Given num = 5, 
# return false.

# 挑战
# Could you solve it without loops/recursion?
class Solution:
    """
    @param num: an integer
    @return: whether the integer is a power of 4
    """
    def isPowerOfFour(self, num):
        # Write your code here
        if num == 1:
            return True
        while num > 1:
            num = num / 4
        if num == 1:
            return True
        else:
            return False
# 不使用循环：151ms，比上面的代码慢
import math
class Solution:
    """
    @param num: an integer
    @return: whether the integer is a power of 4
    """
    def isPowerOfFour(self, num):
        # Write your code here
        if num <= 0:
            return False
        num = math.log10(num) / math.log10(4)
        if num % 1 == 0:
            return True
        else:
            return False
