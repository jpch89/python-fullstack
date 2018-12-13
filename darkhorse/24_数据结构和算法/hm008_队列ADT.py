class Queue:
    """队列"""

    def __init__(self):
        # 队头为 0
        # 队尾为 -1
        self.__list = []

    def enqueue(self, item):
        """入队"""
        self.__list.append(item)

    def dequeue(self):
        """出队"""
        return self.__list.pop(0)

    def is_empty(self):
        """判空"""
        return not self.__list

    def size(self):
        """返回队列大小"""
        return len(self.__list)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

"""
1
2
3
4
"""
