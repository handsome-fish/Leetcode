"""
剑指 Offer 33. 二叉搜索树的后序遍历序列

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。


参考以下这颗二叉搜索树：
     5
    / \
   2   6
  / \
 1   3

示例 1：
输入: [1,6,3,2,5]
输出: false

示例 2：
输入: [1,3,2,6,5]
输出: true

提示：
数组长度 <= 1000
"""
from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        """
        后序遍历：左右根
        二叉搜索树：左 < 根 < 右
        递归左右节点序号
        :param postorder:
        :return:
        """
        if not postorder: return True

        def recur(i, j):
            if i >= j: return True
            m = i
            while postorder[m] < postorder[j]: m += 1
            n = m
            while postorder[n] > postorder[j]: n += 1
            return n == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)
