"""
剑指 Offer 13. 机器人的运动范围


地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，
它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20

链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
solution:
https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/mian-shi-ti-13-ji-qi-ren-de-yun-dong-fan-wei-dfs-b/
"""


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def count(num):
            res = 0
            while num // 10 != 0:
                res += num % 10
                num //= 10
            return res + num

        def dfs(i, j):
            if i >= m or j >= n or (i, j) in visited or k < count(i) + count(j):
                # print(i, count(i), j, count(j), k)
                return 0
            visited.add((i,j))
            return 1 + dfs(i, j + 1) + dfs(i + 1, j)

        visited = set()
        return dfs(0, 0)


s = Solution()
m = 2
n = 3
k = 1
print(s.movingCount(m, n, k))
