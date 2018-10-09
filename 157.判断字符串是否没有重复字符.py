# 实现一个算法确定字符串中的字符是否均唯一出现

# 样例
# 给出"abc"，返回 true
# 给出"aab"，返回 false

# 挑战
# 如果不使用额外的存储空间，你的算法该如何改变？
# 1007ms，最优时间600ms
class Solution:
    """
    @param: str: A string
    @return: a boolean
    """
    def isUnique(self, str):
        # write your code here
        length = len(str)
        if length <= 1:
            return True
        i, j = 0, 1
        while i < length - 1:
            if str[i] == str[j]:
                return False
            else:
                j += 1
                if j == length:
                    i += 1
                    j = i + 1
                    if i == length - 1:
                        return True
