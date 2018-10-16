class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        sentence = s.split()
        res = ""
        
        for i, word in enumerate(sentence):
            res = res + word[::-1] + " "
        
        return res.strip()
