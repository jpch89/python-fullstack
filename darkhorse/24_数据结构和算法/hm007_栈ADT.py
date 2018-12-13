class Stack:
    """栈"""
    def __init__(self):
        self.__list = []

    def push(self, item):
        """压栈"""
        # 尾部作为栈顶，因为对于顺序表，尾部存取更快。
        # 如果使用单链表，应该把头部当做栈顶。
        self.__list.append(item)

    def pop(self):
        """弹栈"""
        return self.__list.pop()

    def peek(self):
        """查看栈顶元素"""
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        """判断栈是否为空"""
        # return not len(self.__list)  # 我的写法
        # return not self.__list  # 推荐写法
        return self.__list == []

    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
