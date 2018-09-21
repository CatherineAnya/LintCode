# 题目描述：计算链表中有多少个结点
# 输入：一个链表
# 输出：链表的结点个数
# 样例：1->3->5 --> 3
############
# 题目分析：考察Python数据结构之链表
# 1. 首先要了解链表的定义
# 2. 其次要知道如何使用Python来创建一个链表
# 3. 最后使用循环并计数计算出链表的结点个数
############
# 知识点：
# 1. 链表的定义：由一组数据项组成的集合，每个数据项都是链表结点的一部分，每个链表结点还包括一个指向下一个结点的指针(链接)
# 2. 在创建链表时，除了链表结点中的指针外，还需要一个指针从head开始，随着链表结点的添加而指向当前结点，来判断下一个结点是否为None
############
# LintCode上代码
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: the first node of linked list.
    @return: An integer
    """
    def countNodes(self, head):
        # write your code here
        count = 0
        while head:
            count += 1
            head = head.next
        return count
############
# Pycharm上代码
# 创建链表->创建链表中的结点->定义计数器循环计数->返回链表结点个数
class ListNode:
    # 创建链表结点类
    def __init__(self, val):
        self.val = val
        self.next = None
class Chain:
    # 创建链表类
    def __init__(self):
        self.head = None
    def createChain(self, val):
        # 创建链表
        listnode = ListNode(val)
        # 创建链表结点
        if self.head is None:
            self.head = listnode
        else:
            p = self.head
            while p.next is not None:
                p = p.next
            p.next = listnode
class Solution:
    """
    @param head: the first node of linked list.
    @return: An integer
    """
    def countNodes(self, head):
        # write your code here
        count = 0
        while head:
            count += 1
            head = head.next
        return count
if __name__ == '__main__':
    chain = Chain()
    N = int(input('Enter the number of nodes in the chain table:'))
    for i in range(N):
        value = int(input('Enter the value of nodes in the chain table:'))
        chain.createChain(value)
    s = Solution()
    print(s.countNodes(chain.head))
