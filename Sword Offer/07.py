"""
剑指 Offer 07. 重建二叉树

输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。


例如，给出
前序遍历 preorder =[3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

限制：

0 <= 节点个数 <= 5000

链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
Solution:
https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/solution/mian-shi-ti-07-zhong-jian-er-cha-shu-di-gui-fa-qin/
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def recur(root, left, right):
            """
            :param root: 在preorder里的索引，代表该子树的根
            :param left: 在inorder里的索引，代表该子树的左子树开头
            :param right: 在inorder里的索引，代表该子树的右子树结尾
            :return: 返回该子树
            """
            if left > right:
                return
            tree = TreeNode(preorder[root])
            i = inorder_hash[preorder[root]]
            tree.left = recur(root + 1, left, i - 1)
            left_size = i - left
            tree.right = recur(root + left_size + 1, i + 1, right)
            return tree

        l = len(inorder)
        inorder_hash = {}
        for i in range(l):
            inorder_hash[inorder[i]] = i
        return recur(0, 0, l - 1)


pre = [3, 9, 20, 15, 7]
in_ = [9, 3, 15, 20, 7]
s = Solution()
print(s.buildTree(preorder=pre, inorder=in_))
