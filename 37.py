class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here
        self.number = number
        num = str(self.number)
        num = num[::-1]
        num = int(num)
        return num
