#
# 在输入数组中的查找所在元素的位置以及查找次数,返回格式String ："i,c"  (i为元素下表，c为查找次数)
# @param arr int整型一维数组 数组
# @param key int整型 待查找的元素
# @return string字符串
#
class Solution:
    def binSearch(self, arr, key):
        def recur(low, high, n):
            if low > high: return -1
            p = int((high + low) / 2)
            if arr[p] > key:
                high = p - 1
                n += 1
                return recur(low, high, n)
            elif arr[p] < key:
                low = p + 1
                n += 1
                return recur(low, high, n)
            else:
                return str(p) + "," + str(n)

        low, high, n = 0, len(arr) - 1, 1
        return recur(low, high, n)

s = Solution()
print(s.binSearch([1, 2, 3, 4, 5], 5))
