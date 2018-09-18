# 题目描述：将一个字符由小写字母转换为大写字母
# 输入：一个小写字母（a~z）
# 输出：相应的大写字母（A~Z）
# 样例：a --> A，b --> B
############
# 题目分析：字母转换，使用Python字符串中的upper()方法和lower()方法
############
# 知识点：
# 1. str.upper()：Python方法，将字符串中的小写字母转为大写字母
# 2. str.lower()：Python方法，将字符串中的大写字母转为小写字母
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
