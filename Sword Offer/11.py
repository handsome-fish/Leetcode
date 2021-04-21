"""
剑指 Offer 11. 旋转数组的最小数字

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组[3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0

链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
"""
from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left, right = 0, len(numbers) - 1
        while left < right:
            m = left + (right - left) // 2
            if numbers[m] > numbers[right]:
                left = m + 1
            elif numbers[m] < numbers[right]:
                right = m
            else:
                # 无法判断m在哪个排序数组中，即无法判断旋转点x在[i, m]还是[m + 1, j]区间中。执行j = j - 1缩小判断范围
                right -= 1
        return numbers[left]


nums = [2, 2, 2, 0, 1]
s = Solution()
print(s.minArray(numbers=nums))
