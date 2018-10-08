# Given an integer, write a function to determine if it is a power of three.
# 挑战
# Could you do it without using any loop / recursion?
class Solution:
    """
    @param n: an integer
    @return: if n is a power of three
    """
    def isPowerOfThree(self, n):
        # Write your code here
        if n == 1:
            return True
        while n > 1:
            n = n / 3
        if n == 1:
            return True
        else:
            return False
