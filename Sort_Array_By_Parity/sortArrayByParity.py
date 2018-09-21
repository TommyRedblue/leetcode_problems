class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        evens = []
        odds = []
        
        for num in A:
            if(self.isEven(num) == True):
                evens.append(num)
            else:
                odds.append(num)
                
        return evens + odds
        
    
    def isEven(self, n):
        if n%2 == 0:
            return True
        else:
            return False
