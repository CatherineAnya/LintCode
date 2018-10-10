# 编译错误
class Solution:
    """
    @param words: the given list of words
    @return: the number of different transformations among all words we have
    """
    def uniqueMorseRepresentations(self, words):
        # Write your code here
        dictionary = {
            'a': '.-',
            'b': '-...',
            'c': '-.-.', 
            'd': '-..',
            'e': '.',
            'f': '..-',
            'g': '--.',
            'h': '....',
            'i': '..',
            'j': '.---',
            'k': '-.-', 
            'l': '.-..',
            'm': '--',
            'n': '-.',
            'o': '---',
            'p': '.--.',
            'q': '--.-',
            'r': '.-.',
            's': '...',
            't': '-',
            'u': '..-',
            'v': '...-',
            'w': '.--',
            'x': '-..-',
            'y': '-.--',
            'z': '--..'
        }
        morse = list()
        m = ''
        for i in words:
            for j in i:
                m += dictionary[j]
            morse.append(m)
        x， y = 0, 1
        while x <= len(morse)-1:
            if morse[x] == morse[y]:
                morse.pop(x)
                y = x + 1
            else:
                y += 1
                if y == len(morse):
                    x += 1
                    y = x + 1
        return len(morse)
