class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        if n <= 0:
            return 0
        f = list()
        f.append(0)
        f.append(1)
        for i in range(n):
            if len(f) < (i+1):
                f.append(f[i-1]+f[i-2])
        return f[n-1]
