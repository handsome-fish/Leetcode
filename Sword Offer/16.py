"""
剑指 Offer 16. 数值的整数次方

实现pow(x,n)，即计算 x 的 n 次幂函数（即，x^n）。不得使用库函数，同时不需要考虑大数问题。


示例 1：

输入：x = 2.00000, n = 10
输出：1024.00000
示例 2：

输入：x = 2.10000, n = 3
输出：9.26100
示例 3：

输入：x = 2.00000, n = -2
输出：0.25000
解释：2^(-2) = 1/22 = 1/4 = 0.25

提示：

-100.0 <x< 100.0
-231<= n <=231-1
-104<= xn<= 104


链接：https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof
solution:
https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/solution/mian-shi-ti-16-shu-zhi-de-zheng-shu-ci-fang-kuai-s/
"""


# x, n = 0.00001, 2147483647 超时
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if x == 0:
#             return 0
#         if n == 0:
#             return 1
#
#         def binMul(n, x):
#             if n == 1:
#                 return x
#             if n == -1:
#                 return 1/x
#             mid = n // 2
#             if n % 2 == 0:
#                 return binMul(mid, x) * binMul(mid, x)
#             else:
#                 return x * binMul(mid, x) * binMul(mid, x)
#
#         return binMul(n, x)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        res = 1
        if n < 0:
            x, n = 1 / x, -n
        while n:
            if n & 1:
                # 奇数需要多乘一个x
                res *= x
            x *= x
            # 除2
            n >>= 1
        return res


s = Solution()
x, n = 0.00001, 2147483647
print(s.myPow(x, n))
