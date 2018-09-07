class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0;
        
        for let in S:
            if let in J:
                count = count + 1
        
        return count
