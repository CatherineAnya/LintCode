class Solution:
    """
    @param character: a character
    @return: a character
    """
    def lowercaseToUppercase(self, character):
        # write your code here
        self.character = character
        char = str.upper(self.character)
        return char
