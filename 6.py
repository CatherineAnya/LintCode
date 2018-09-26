class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        newArray = list()
        for i in A:
            newArray.append(i)
        for j in B:
            newArray.append(j)
        newArray.sort()
        return newArray
