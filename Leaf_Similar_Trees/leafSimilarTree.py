# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        r1_leaves = []
        self.dfs(root1, r1_leaves)
        r2_leaves = []
        self.dfs(root2, r2_leaves)
        
        return r1_leaves == r2_leaves
        
    def dfs(self,root, leaves):
        if root != None:
            if root.left == None and root.right == None:
                leaves.append(root.val)
            self.dfs(root.left, leaves)
            self.dfs(root.right, leaves)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
