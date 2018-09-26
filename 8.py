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
    string = input('Enter a string:')
    o = int(input('Enter offset:'))
    s = Solution()
    print(s.rotateString(string, o))
    
LintCode 编辑器竟然不支持切片操作 :=(
再想想
