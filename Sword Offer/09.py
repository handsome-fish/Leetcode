"""
剑指 Offer 09. 用两个栈实现队列

用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead操作返回 -1 )


示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
提示：

1 <= values <= 10000
最多会对appendTail、deleteHead 进行10000次调用


链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
"""


class CQueue:

    def __init__(self):
        self.A_stack, self.B_stack = [], []

    def appendTail(self, value: int) -> None:
        self.A_stack.append(value)

    def deleteHead(self) -> int:
        if len(self.A_stack) == 0:
            return -1
        if self.B_stack:
            return self.B_stack.pop()
        while self.A_stack:
            self.B_stack.append(self.A_stack.pop())
        return self.B_stack.pop()


# Your CQueue object will be instantiated and called as such:
obj = CQueue()
obj.appendTail(3)
param_2 = obj.deleteHead()
print(param_2)
