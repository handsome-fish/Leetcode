# 整数反转可以通过除法和余数操作得到
# 正数和负数要分开考虑
# python负数取余向大取的  -123%10=7
# python只有int整数最大值函数，需要import sys

# 注意：如果用字符串解的话，可用s=s[::-1]操作将字符串反转

def reverse(x):
    # 设置一个标志变量，判断是否为负数
    flag = False
    if x < 0:
        flag = True
    # 将x按正数计算
    x = abs(x)
    # 返回值
    res = 0
    while(x != 0):
        res = res*10 + x%10
        x /= 10
        x = int(x)
    res = res if flag==False else (-1*res)
    # 判断是否溢出
    res = res if res <= pow(2,31)-1 and res >= -1*pow(2,31) else 0
    return res

if __name__=="__main__":
    x = 1534236469
    x = reverse(x)
    print(x)
