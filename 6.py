# 68ms
class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        len1 = len(A)
        len2 = len(B)
        i, j = 0, 0
        C = list()
        while i < len1 and j < len2:
            if A[i] < B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        while i < len1:
            C.append(A[i])
            i += 1
        while j < len2:
            C.append(B[j])
            j += 1
        return C
    
# 101ms
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
    
# 105ms
class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        for j in B:
            A.append(j)
        A.sort()
        return A
