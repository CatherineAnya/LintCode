# coding=utf-8
class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        # write your code here
        length = len(str)
        offset = offset % length
        if offset == 0:
            return str
        offsetStr = str[-offset::]
        newStr = str[:(length - offset):]
        return offsetStr + newStr
if __name__ == '__main__':
    N = int(input('Enter an integer:'))
    charArray = list()
    for i in range(N):
        charArray.append(input('Enter a char:'))
    o = int(input('Enter offset:'))
    s = Solution()
    print(s.rotateString(charArray, o))

# 701ms
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
        del str[:]
        str.extend(list2)
        str.extend(list1)
        return str
