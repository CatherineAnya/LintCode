# 题目描述：在二叉树中寻找值最大的节点并返回该结点
# 输入：一棵二叉树
# 输出：值最大的结点
# 样例：{1,-5,3,1,2,-4,-5} --> 3
############
# 题目分析：考察Python数据结构之二叉树
# 1. 首先要了解二叉树的定义
# 2. 其次要知道如何使用Python创建一个二叉树
# 3. 最后要使用递归遍历二叉树得出最大值结点
############
# 知识点：
# 1. 二叉树的定义(一)：数据结构中树的一种，是由n(n>=0)个结点组成的有限集合
# 2. 二叉树的定义(二)：二叉树或者为空，或者由一个被称为根结点(root)的元素及两个互不相交的、分别被称为左子树和右子树的二叉树组成
# 3. 二叉树的特点(一)：每个结点最多有二棵子树(度<=2)，并且子树必须有左右之分
# 4. 二叉树的特点(二)：第i层最多有2^(i-1)个结点
# 5. 二叉树的特点(三)：深度(层数)为k的二叉树最多有2^k-1个结点
# 6. 二叉树的特点(四)：任何一棵二叉树，如果其终端结点个数为N0，度为2的结点个数为N2，则N0=N2+1
# 7. 
# 8. 
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
    
class TreeNode:
    # 创建结点类
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Tree:
    # 创建树类
    def __init__(self):
        self.root = None
    def create(self, val):
        node = TreeNode(val)
        if self.root is None:
            self.root = node
        else:
            queue = [self.root]
            while True:
                childnode = queue.pop(0)
                if childnode.left is None:
                    childnode.left = node
                    return
                elif childnode.right is None:
                    childnode.right = node
                    return
                else:
                    queue.append(childnode.left)
                    queue.append(childnode.right)
if __name__ == '__main__':
    tree = Tree()
    N = int(input('Enter the number of nodes in the binary tree:'))
    for i in range(N):
        value = int(input('Enter the value of nodes in the binary tree:'))
        print(tree.create(value))
