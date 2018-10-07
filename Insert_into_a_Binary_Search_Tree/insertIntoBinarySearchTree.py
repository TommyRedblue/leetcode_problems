# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        r = TreeNode(val)        
        if root is None:
            return r
        else:
            self.insertNode(root, r)
        
        return root
        
        
    def insertNode(self, root, node):
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                self.insertNode(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                self.insertNode(root.left, node)
        
