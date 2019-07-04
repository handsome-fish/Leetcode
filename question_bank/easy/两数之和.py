# 该题用一遍哈希表思想，用python字典解决

def twoSum(nums, target):
    # 建一个空字典
    dic = {}
    n = 0
    for num in nums:
        # 判断差值是否在字典中
        if target - num in dic:
            return dic[target-num], n
        # 将值存入key，将index存入value
        dic[num] = n
        n += 1
if __name__=="__main__":
    nums = [3,4,1,4,-5]
    target = 5
    l = twoSum(nums, target)
    print(l)