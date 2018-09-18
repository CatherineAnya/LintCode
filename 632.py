"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: root: the root of tree
    @return: the max node
    """
    maxnum = -9999
    node = None
    def maxNode(self, root):
        # write your code here
        if root is None:
            return None
        if root.val > self.maxnum:
            self.maxnum = root.val
            self.node = root
        self.maxNode(root.left)
        self.maxNode(root.right)
        return self.node
