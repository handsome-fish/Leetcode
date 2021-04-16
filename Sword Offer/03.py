"""
剑指 Offer 03. 数组中重复的数字

找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3


限制：

2 <= n <= 100000


链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
"""
from collections import defaultdict
from typing import List





class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for num in nums:
            if dic.__contains__(num):
                return num
            dic[num] += 1

    def best_answer(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if num in s:
                return num
            s.add(num)

s = Solution()
print(s.findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))
print(s.best_answer([2, 3, 1, 0, 2, 5, 3]))
