# 题目描述：给一个整数n，从1到n按照规则打印每个数
# 规则：若这个数被3整除，打印fizz；若这个数被5整除，打印buzz；若这个数同时被3和5整除，打印fizz buzz
# 输入：整数n
# 输出：符合规则的字符串数组
# 样例：n=15 --> ["1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz", "11", "fizz", "13", "14", "fizz buzz"]
# 挑战：仅使用一个if语句解决该问题
############
# 题目分析：
############
# 知识点：
# 1. 
# 2. 
############
# if…elif…else嵌套
class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        # write your code here
        strArray = list()
        for i in range(1, n+1):
            if i % 15 == 0:
                strArray.append('fizz buzz')
            elif i % 3 == 0:
                strArray.append('fizz')
            elif i % 5 == 0:
                strArray.append('buzz')
            else:
                strArray.append(str(i))
        return strArray
if __name__ == '__main__':
    N = int(input('Enter a integer:'))
    s = Solution()
    print(s.fizzBuzz(N))
############
# 仅用一个if语句
