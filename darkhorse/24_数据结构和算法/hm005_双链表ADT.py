from hm004_单链表ADT import SinglyLinkedList


class Node:
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.prev = None
        self.next = None


class DoublyLinkedList(SinglyLinkedList):
    """双链表"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        cur = self.__head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur:
            print(cur.elem, end=' ')
            cur = cur.next
        print()

    def add(self, item):
        """头部添加元素"""
        node = Node(item)
        self.__head.prev = node
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """指定位置添加节点。
        :param pos 从 0 开始
        """
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            cur.prev.next = node
            node.prev = cur.prev
            node.next = cur
            cur.prev = node

    def search(self, item):
        cur = self.__head
        while cur:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, item):
        cur = self.__head
        while cur:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        # 判断链表是否只有一个节点
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        # 判断是否是最后一个节点
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next


if __name__ == '__main__':
    dll = SinglyLinkedList()
    print(dll.is_empty())
    print(dll.length())

    dll.append(1)
    print(dll.is_empty())
    print(dll.length())

    dll.append(2)
    dll.add(8)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)
    # 8 1 2 3 4 5 6
    dll.insert(-1, 9)  # 9 8 1 2 3 4 5 6
    dll.travel()

    dll.insert(2, 100)  # 9 8 100 1 2 3 4 5 6
    dll.travel()

    dll.insert(10, 200)  # 9 8 100 1 2 3 4 5 6 200
    dll.travel()

    dll.remove(100)
    dll.travel()

    dll.remove(9)
    dll.travel()

    dll.remove(200)
    dll.travel()

"""
True
0
False
1
9 8 1 2 3 4 5 6
9 8 100 1 2 3 4 5 6
9 8 100 1 2 3 4 5 6 200
9 8 1 2 3 4 5 6 200
8 1 2 3 4 5 6 200
8 1 2 3 4 5 6
"""
