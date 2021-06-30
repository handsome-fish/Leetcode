"""
下一个排列

实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须 原地 修改，只允许使用额外常数空间。

示例 1：
输入：nums = [1,2,3]
输出：[1,3,2]

示例 2：
输入：nums = [3,2,1]
输出：[1,2,3]

示例 3：
输入：nums = [1,1,5]
输出：[1,5,1]

示例 4：
输入：nums = [1]
输出：[1]

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 100

链接：https://leetcode-cn.com/problems/next-permutation
"""
from typing import List

def next_permutation(nums:List[int]):
    """
    从数组倒着查找，找到nums[j] 比nums[j-1]大的时候
    :param nums:
    :return:
    """
    if len(nums) == 0 or len(nums) == 1: return
    i = j = len(nums) - 1
    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1
    # 已经是最大的排序，那么将数组翻转
    if i == 0:
        nums.reverse()
        return
    while nums[j] <= nums[i - 1]:
        j -= 1
    # 交换大小数
    nums[j], nums[i-1] = nums[i-1], nums[j]
    k = len(nums) - 1
    # 交换后，将大数后面的数组倒序排列
    while i <= k:
        nums[i], nums[k] = nums[k], nums[i]
        i += 1
        k -= 1


next_permutation([1,3,2])


