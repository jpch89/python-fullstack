class Deque:
    """双端队列"""
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        # 列表的头就是双端队列的头
        self.__list.insert(0, item)

    def add_rear(self, item):
        self.__list.append(item)

    def remove_front(self):
        return self.__list.pop(0)

    def remove_rear(self):
        return self.__list.pop()

    def is_empty(self):
        return not self.__list

    def size(self):
        return len(self.__list)

if __name__ == '__main__':
    deque = Deque()
    deque.add_front(1)
    deque.add_front(2)
    deque.add_rear(3)
    deque.add_rear(4)
    print(deque.size())
    print(deque.remove_front())
    print(deque.remove_front())
    print(deque.remove_rear())
    print(deque.remove_rear())

"""
4
2
1
4
3
"""
