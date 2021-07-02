"""
剑指 Offer 39. 数组中出现次数超过一半的数字

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2

限制：
1 <= 数组长度 <= 50000
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        threshold = len(nums) // 2 + 1
        for num in nums:
            if num not in dic.keys():
                dic[num] = 1
            else:
                dic[num] += 1
            if dic[num] == threshold:
                return num


s = Solution()
arr = [1, 2, 3, 2, 2, 2, 5, 4, 2]
print(s.majorityElement(arr))
