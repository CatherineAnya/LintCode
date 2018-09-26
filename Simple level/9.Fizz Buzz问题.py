# 题目描述：给一个整数n，从1到n按照规则打印每个数
# 规则：若这个数被3整除，打印fizz；若这个数被5整除，打印buzz；若这个数同时被3和5整除，打印fizz buzz
# 输入：整数n
# 输出：符合规则的字符串数组
# 样例：n=15 --> ["1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz", "11", "fizz", "13", "14", "fizz buzz"]
# 挑战：仅使用一个if语句解决该问题
############
# 题目分析：
# 思路一：使用一个for循环和三个if语句来解决，其中被3和5整除可以看做被15整除，并且要写在第一个if语句中，防止被其余两个if语句所包含
# 思路二：使用for循环以及字符串截取和逻辑运算符or来解决，其中仅用一个if语句把"fizzbuzz"改为"fizz buzz"即可
# 思路三：对一个数取余的结果一定小于这个数，因此使用一个列表把能被3、5、15整除的数存为固定的字符串，其他数存为None，再使用for循环和一个if语句来解决
############
# 知识点：
# 1. 逻辑运算符：运算数据都为布尔类型时，逻辑运算思路相同，若运算数据中存在非布尔类型，思路就不同了
# 2. and：布尔与，若运算数据中存在False，则返回False；否则，返回最右边数据
# 3. or：布尔或，若运算数据中存在False，则返回另一个数据；否则，返回最左边数据
# 4. not：布尔非，若运算数据为True，则返回False；若运算数据为False，则返回True
# 5. 列表生成式：Python内置的用来创建列表的生成式，可以用一行语句代替循环生成列表，例如：strMap = [None for i in range(15)]
############
# if…elif…else语句
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
# 方法一：
class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        # write your code here
        strArray = list()
        for i in range(1, n+1):
            strArray.append("fizz"[(i % 3) * 4::] + "buzz"[(i % 5) * 4::] or str(i))
            if strArray[i-1] == 'fizzbuzz':
                strArray[i-1] = 'fizz buzz'
        return strArray
if __name__ == '__main__':
    N = int(input('Enter a integer:'))
    s = Solution()
    print(s.fizzBuzz(N))
############
# 方法二：
class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        # write your code here
        # strMap = [None for i in range(15)]
        strMap = list()
        for i in range(15):
            strMap.append(None)
        strMap[0] = 'fizz buzz'
        strMap[3] = strMap[6] = strMap[9] = strMap[12] = 'fizz'
        strMap[5] = strMap[10] = 'buzz'
        strArray = list()
        for x in range(1, n+1):
            if strMap[x % 15] is not None:
                strArray.append(strMap[x % 15])
            else:
                strArray.append(str(x))
        return strArray
if __name__ == '__main__':
    N = int(input('Enter a integer:'))
    s = Solution()
    print(s.fizzBuzz(N))
