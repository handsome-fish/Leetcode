"""
剑指 Offer 14- I. 剪绳子

给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 ×3 ×4 = 36
提示：

2 <= n <= 58

链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof
solution:
https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/mian-shi-ti-14-i-jian-sheng-zi-tan-xin-si-xiang-by/
"""
import math


class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n-1
        # 通过数学推导可知，让绳子尽量以长度3等分，是乘积最大的。剩下的一段如果为2，那就不分；如果为1，就拿出一段3，组成2*2>3*1
        number, remain = n // 3, n % 3
        if remain == 0:
            return int(math.pow(3, number))
        if remain == 1:
            return int(math.pow(3, number - 1) * 2 * 2)
        return int(math.pow(3, number) * 2)


s = Solution()
n = 10
print(s.cuttingRope(n))
