

def dfs(s, path, res):
    if s == s[::-1]:
        path.append(s)
        res.append(path[:])
        path.pop()
    for i in range(1, len(s)):
        a = s[:i]
        if a == a[::-1]:
            path.append(a)
            dfs(s[i:], path, res)
            path.pop()


def partition(s):
    res = []
    dfs(s, [], res)
    return res


if __name__ == "__main__":
    s = "aabb"
    print(partition(s))
