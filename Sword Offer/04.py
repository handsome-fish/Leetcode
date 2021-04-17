"""
剑指 Offer 04. 二维数组中的查找

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。



示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target=5，返回true。

给定target=20，返回false。


限制：

0 <= n <= 1000

0 <= m <= 1000

链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof
"""
from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        i, j = len(matrix) - 1, 0
        print(len(matrix))
        print(len(matrix[0]))
        while i >= 0 and j <= len(matrix[0]) - 1:
            if target < matrix[i][j]:
                i -= 1
                continue
            elif target > matrix[i][j]:
                j += 1
                continue
            else:
                return True
        return False


# mat, tar = [
#                [1, 4, 7, 11, 15],
#                [2, 5, 8, 12, 19],
#                [3, 6, 9, 16, 22],
#                [10, 13, 14, 17, 24],
#                [18, 21, 23, 26, 30]
#            ], 30

mat, tar = [[-1,3]], 3

s = Solution()
print(s.findNumberIn2DArray(matrix=mat, target=tar))
