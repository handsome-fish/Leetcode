"""
剑指 Offer 34. 二叉树中和为某一值的路径

输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

示例:
给定如下二叉树，以及目标和 target = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:
[
   [5,4,11,2],
   [5,8,4,5]
]

提示：
节点总数 <= 10000

Solution:
https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/solution/mian-shi-ti-34-er-cha-shu-zhong-he-wei-mou-yi-zh-5/
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        def dfs(sum_num, node: TreeNode):
            if not node: return
            sum_num += node.val
            tmp.append(node.val)
            if sum_num == target and not node.left and not node.right:
                """
                值得注意的是，记录路径时若直接执行 res.append(path) ，则是将 path 对象加入了 res
                后续 path 改变时， res 中d的path 对象也会随之改变
                正确做法：res.append(list(path)) ，相当于复制了一个 path 并加入到 res
                """
                res.append(list(tmp))
            dfs(sum_num, node.left)
            dfs(sum_num, node.right)
            tmp.pop()
            print(tmp)

        tmp, res = [], []
        dfs(0, root)
        return res


t = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
             TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
s = Solution()
s.pathSum(t, 22)
