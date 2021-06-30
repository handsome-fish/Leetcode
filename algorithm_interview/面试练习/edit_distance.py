"""
最短编辑距离
"""


def edit_length(str1, str2):
    if not str1: return len(str2)
    """
    构建len(str1)+1*len(str2)+1的矩阵，第一行和第一列初始化为列序号和行序号，中间列和行随便初始化即可
    dp[i - 1][j] + 1表示删掉字符串a最后一个字符a[i]
    dp[i][j - 1] + 1表示给字符串添加b最后一个字符
    dp[i - 1][j - 1] + cost表示改变, 相同则不需操作次数, 不同则需要, 用cost记录
    """
    dp = [[i + j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
    for idx1 in range(1, len(str1) + 1):
        for idx2 in range(1, len(str2) + 1):
            cost = 0 if str1[idx1 - 1] == str2[idx2 - 1] else 1
            print(dp)
            dp[idx1][idx2] = min(dp[idx1 - 1][idx2] + 1, dp[idx1][idx2 - 1] + 1, dp[idx1 - 1][idx2 - 1] + cost)
    print(dp)
    return dp[len(str1)][len(str2)]


str1 = "coffee"
str2 = "cafe"

print(edit_length(str1, str2))
