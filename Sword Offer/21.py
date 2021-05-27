"""
剑指 Offer 21. 调整数组顺序使奇数位于偶数前面

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。


示例：
输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。


提示：
0 <= nums.length <= 50000
1 <= nums[i] <= 10000
"""

from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] & 1:
                # 奇数
                i += 1
                continue
            if not nums[j] & 1:
                # 偶数
                j -= 1
                continue
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1
        return nums


s = Solution()
nums = [1, 2, 3, 4]
print(s.exchange(nums))
