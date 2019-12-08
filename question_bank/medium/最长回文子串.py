# 该程序用动态规划算法
# 判断回文串可用判断s == s[::-1]


def longestPalindrome(s):
    length = len(s)
    # 如果本身为回文数,则直接返回
    if s == s[::-1]:
        return s
    # 设置最大长度和开始索引
    max_len, begin = 1, 0
    for i in range(1, length):
        odd = s[i - max_len - 1:i + 1]
        even = s[i - max_len:i + 1]
        if i - max_len >= 1 and odd == odd[::-1]:
            begin = i - max_len - 1
            max_len += 2
            continue
        if i - max_len >= 0 and even == even[::-1]:
            begin = i - max_len
            max_len += 1
    return s[begin:begin + max_len]


if __name__ == "__main__":
    s = "abaa"
    s = longestPalindrome(s)
    print(s)
