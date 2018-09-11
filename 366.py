编译器：
class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
        
pycharm：
# encoding=utf-8
# 查找斐波那契数列中的第N个数
# 例子：1 --> 0，2 -- > 1，10 --> 34
def Fibonacci(n):
    if n <= 1:
        return n
    return Fibonacci(n-1)+Fibonacci(n-2)
n = int(input('Enter a digit number:'))
if n <= 0:
    print('输入正整数')
else:
    print(Fibonacci(n-1))
