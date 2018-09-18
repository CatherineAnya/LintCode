# 题目描述：将一个字符由小写字母转换为大写字母
# 输入：一个小写字母（a~z）
# 输出：相应的大写字母（A~Z）
# 样例：a --> A，b --> B
##########
# 题目分析：
##########
# 知识点：
# 1. 
# 2. 
class Solution:
    """
    @param character: a character
    @return: a character
    """
    def lowercaseToUppercase(self, character):
        # write your code here
        return str.upper(character)
if __name__ == '__main__':
    char = input('Enter a lowercase character:')
    s = Solution()
    print(s.lowercaseToUppercase(char))
