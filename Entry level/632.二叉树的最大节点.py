# 题目描述：在二叉树中寻找值最大的节点并返回该节点
# 输入：一棵二叉树
# 输出：值最大的节点
# 样例：{1,-5,3,1,2,-4,-5} --> 3
############
# 题目分析：
############
# 知识点：
# 1.
# 2.
# 3.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
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
