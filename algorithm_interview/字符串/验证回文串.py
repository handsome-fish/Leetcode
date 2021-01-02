

def isPalindrome1(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

def isPalindrome2(s):
    if s == "":
        return True
    i = 0
    j = len(s) - 1
    s = s.lower()
    while i <= j:
        if not s[i].isalnum():
            i = i + 1
            continue
        if not s[j].isalnum():
            j = j - 1
            continue
        if s[i] == s[j]:
            i = i + 1
            j = j - 1
            continue
        else:
            return False
    return True


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome1(s))
