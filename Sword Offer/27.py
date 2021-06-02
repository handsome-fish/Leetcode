"""
剑指 Offer 27. 二叉树的镜像

请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：
     4
   /   \
  2     7
 / \   / \
1   3 6   9

镜像输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1


示例 1：
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]

限制：
0 <= 节点个数 <= 1000
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def mirrorTree(self, root: TreeNode) -> TreeNode:
    #     """
    #     递归，自下而上交换
    #     :param root:
    #     :return:
    #     """
    #     if not root: return root
    #     temp = root.left
    #     root.left = self.mirrorTree(root.right)
    #     root.right = self.mirrorTree(temp)
    #     return root

    def mirrorTree(self, root: TreeNode) -> TreeNode:
        """
        栈遍历交换
        :param root:
        :return:
        """
        if not root: return root
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            node.left, node.right = node.right, node.left
        return root
