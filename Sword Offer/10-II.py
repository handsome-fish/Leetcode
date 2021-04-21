"""
剑指 Offer 10- II. 青蛙跳台阶问题

一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
示例 2：

输入：n = 7
输出：21
示例 3：

输入：n = 0
输出：1
提示：

0 <= n <= 100

链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
"""


class Solution:
    def numWays(self, n: int) -> int:
        if n < 2:
            return 1
        f1, f2 = 1, 1
        for _ in range(n):
            f1, f2 = f2, f1 + f2
        return f1 % 1000000007


n = 45
s = Solution()
print(s.numWays(n=n))
