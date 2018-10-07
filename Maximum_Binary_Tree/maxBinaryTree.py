class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        return self.makeNode(nums, 0, len(nums))
    
    def makeNode(self, nums, l, r):
        if l == r:
            return None
        
        max_i = self.maxInRange(nums, l, r)
        root = TreeNode(nums[max_i])
        root.left = self.makeNode(nums, l, max_i)
        root.right = self.makeNode(nums, max_i + 1, r)
        return root
        
    def maxInRange(self, nums, l, r):
        max_i = l
        
        for i, n in enumerate(nums, l):
            if i >= r:
                break
            if nums[max_i] < nums[i]:
                max_i = i
        print(max_i)
        return max_i
        
