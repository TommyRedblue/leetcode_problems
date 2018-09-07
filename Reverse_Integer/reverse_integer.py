class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        isNeg = False
        string_x = str(x)[::-1]
        
        if "-" in string_x:
            isNeg = True
        
        string_x = string_x.replace("-", "")
        
        if isNeg is True:
            string_x = "-" + string_x
        
        if int(string_x) > 2147483647 or int(string_x) < -2147483648:
            return 0
        
        return int(string_x)
        
        
