"""
采用动态规划，遍历字符串，判断每个子字符串能否被分割，flag[i]表示s中前i个字符是否可以被dict中的字符串表示，
递推关系为if flag[j]==true && s[j:i] in wordDict:flag[i]=1, 最后判断flag[s.size()]是否为1
"""

def wordBreak(s, wordDict):
    l = len(s)
    flag = [False] * (l + 1)
    flag[0] = True
    for i in range(l):
        for j in range(i+1, l+1):
            if flag[i] and s[i:j] in wordDict:
                flag[j] = True
    return flag[-1]


if __name__ == "__main__":
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(wordBreak(s, wordDict))
