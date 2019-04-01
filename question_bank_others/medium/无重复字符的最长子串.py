# 用字典存储字符及其索引

def lengthOfLongestSubstring(s):
    # 设置最大长度
    max_len = 0
    # 初始化字典
    dic = {}
    # 设置索引
    start = 0
    for i in range(len(s)):
        # 如果该字符在字典中，更新索引到重复字符后面一个字符处
        if s[i] in dic and dic[s[i]] >= start:
            start = dic[s[i]] + 1
        # 将该字符存到字典中
        dic[s[i]] = i
        # 更新最大长度
        max_len = max(max_len, i - start + 1)
    return max_len

if __name__=="__main__":
    s = "pwwkew"
    max_len = lengthOfLongestSubstring(s)
    print(max_len)