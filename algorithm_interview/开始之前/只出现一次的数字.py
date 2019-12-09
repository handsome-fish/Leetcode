# 通过初始化并计数的方式找出，线性遍历两遍，比较慢
def singleNumber1(nums):
    dic = dict.fromkeys(nums, 0)
    for num in nums:
        dic[num] = dic[num] + 1
    for num in nums:
        if dic[num] == 1:
            return num


# 字典中有就删除，没有就插入，剩下的就是单独一个的元素，遍历一次，比较快
def singleNumber2(nums):
    dic = {}
    for num in nums:
        if dic.__contains__(num):
            dic.pop(num)
        else:
            dic[num] = ""
    print(dic)
    return list(dic.keys())[0]


if __name__ == "__main__":
    res = singleNumber2([4, 1, 2, 1, 2])
    print(res)
