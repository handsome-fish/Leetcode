"""
剑指 Offer 42. 连续子数组的最大和

输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)。


示例1:
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

提示：
1 <= arr.length <= 10^5
-100 <= arr[i] <= 100
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        df = [0 for num in nums]
        df[0] = nums[0]
        for i in range(1, len(nums)):
            df[i] = df[i - 1] + nums[i] if df[i - 1] > 0 else nums[i]
        return max(df)


s = Solution()
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(s.maxSubArray(arr))
