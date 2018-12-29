class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        lis = s.split()
        reversed_string = ''
        
        for word in reversed(lis):
            reversed_string += word + ' '
            
        return reversed_string.strip()
        
