# 超出时间限制
class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        count = 0
        result = 1
        if n == 0:
            return 1
        for i in range(1, n+1):
            result = result * i
        result = str(result)[::-1]
        for x in range(len(result)):
            if result[x] == '0':
                count = count + 1
            else:
                break
        return count
if __name__ == '__main__':
    N = int(input('Enter an integer:'))
    s = Solution()
    print(s.trailingZeros(N))

# 超出最大递归深度
class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        count = 0
        result = str(self.factorial(n))[::-1]
        for x in range(len(result)):
            if result[x] == '0':
                count += 1
            else:
                break
        return count
    def factorial(self, num):
        if num == 0:
            return 1
        return num * self.factorial(num-1)
if __name__ == '__main__':
    N = int(input('Enter an integer:'))
    s = Solution()
    print(s.trailingZeros(N))
