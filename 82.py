class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        # write your code here
        i, j = 0, 1
        while i < len(A):
            if len(A) == 1:
                return A[0]
            if A[i] != A[j]:
                j += 1
                if j == len(A):
                    return A[i]
            else:
                A.pop(i)
                A.pop(j-1)
                j = 1
if __name__ == '__main__':
    N = int(input('Enter an integer:'))
    intArray = list()
    for i in range(2*N+1):
        intArray.append(input('Enter a integer:'))
    s = Solution()
    print(s.singleNumber(intArray))
