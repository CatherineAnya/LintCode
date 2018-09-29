# 题目描述：给定一个字符串和一个偏移量，根据偏移量旋转字符串(从左向右旋转)
# 输入：一个字符串和一个偏移量
# 输出：旋转后的字符串
# 样例：str='abcdefg'，offset=0 --> str='abcdefg'；str='abcdefg'，offset=3 --> str='efgabcd'
# 挑战：在数组上原地旋转，使用O(1)的额外空间
############
# 题目分析：根据样例理解数组的旋转，即从数组尾部移动偏移量个元素到数组开头
# 注意项：参数str代表一个数组，即输入的字符串要转换为数组；最终输出为字符串，即返回的数组要转换成字符串
# 考虑一：若偏移量大于字符串长度怎么办？偏移量与字符串长度取余，得到的余数就是字符串的偏移量
# 考虑二：若偏移量为0怎么办？做判断，直接返回原字符串
# 考虑三：若字符串长度为0，即字符串为空怎么办？做判断，直接返回原字符串
############
# 知识点：
# 1. list1+list2：两个列表用+连接，合并成一个新列表
# 2. char.join(list)：Python字符串的方法，将序列中的元素以指定的字符连接，生成并返回一个新的字符串
# 3. del：Python的内置函数，删除一个变量，当用于列表操作时，可根据索引删除一个或者连续几个元素
# 4. list[:]=list1+list2：修改列表中所有元素的值
############
# 返回新数组
class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        # write your code here
        length = len(str)
        if length == 0:
            return str
        offset = offset % length
        if offset == 0:
            return str
        offsetStr = str[-offset::]
        newStr = str[:(length - offset):]
        return offsetStr + newStr
if __name__ == '__main__':
    string = input('Enter a string:')
    charArray = list()
    charArray.extend(string)
    o = int(input('Enter offset:'))
    s = Solution()
    print(''.join(s.rotateString(charArray, o)))
############
# 在数组上原地旋转
# 方法一：
class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        # write your code here
        length = len(str)
        if length == 0:
            return str
        offset = offset % length
        if offset == 0:
            return str
        value = length - offset
        list1 = str[:value]
        list2 = str[value:]
        del str[:]
        str.extend(list2)
        str.extend(list1)
        return str
if __name__ == '__main__':
    string = input('Enter a string:')
    charArray = list()
    charArray.extend(string)
    o = int(input('Enter offset:'))
    s = Solution()
    print(''.join(s.rotateString(charArray, o)))
############
# 方法二：(推荐)
class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        # write your code here
        length = len(str)
        if length == 0:
            return str
        offset = offset % length
        value = length - offset
        if offset == 0:
            return str
        list1 = str[:value]
        list2 = str[value:]
        str[:] = list2 + list1
        return str
if __name__ == '__main__':
    string = input('Enter a string:')
    charArray = list()
    charArray.extend(string)
    o = int(input('Enter offset:'))
    s = Solution()
    print(''.join(s.rotateString(charArray, o)))
