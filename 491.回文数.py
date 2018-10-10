# 判断一个正整数是不是回文数。

# 回文数的定义是，将这个数反转之后，得到的数仍然是同一个数。

# 样例
# 11, 121, 1, 12321 这些是回文数。

# 23, 32, 1232 这些不是回文数。

# 注意事项
# 给的数一定保证是32位正整数，但是反转之后的数就未必了。
# 1711ms
class Solution:
    """
    @param num: a positive number
    @return: true if it's a palindrome or false
    """
    def isPalindrome(self, num):
        # write your code here
        strnum = str(num)
        if strnum == strnum[::-1]:
            return True
        else:
            return False
