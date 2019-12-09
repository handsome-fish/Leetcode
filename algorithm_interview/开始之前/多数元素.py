# 累加次数，大于n/2就是多数
def majorityElement1(nums):
    multiLen = len(nums) // 2
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1
        if dic[num] > multiLen:
            return num


# 可以先排序，因为大于n/2个，所以中间那个数一定是多数
def majorityElement2(nums):
    nums.sort()
    return nums[len(nums) // 2]


if __name__ == "__main__":
    res = majorityElement2([2, 2, 1, 1, 1, 2, 2])
    print(res)
