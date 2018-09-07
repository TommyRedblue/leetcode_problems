class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for first, i in enumerate(nums):
          for second, j in enumerate(nums):
            if(((i + j) == target) and (first != second)):
              return [first,second]
        
