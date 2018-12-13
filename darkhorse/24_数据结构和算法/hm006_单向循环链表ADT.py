class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SinglyCircularLinkedList:
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next is not self.__head:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        if self.is_empty():
            return
        cur = self.__head
        while cur.next is not self.__head:
            print(cur.elem, end=' ')
            cur = cur.next
        # 退出循环时，cur 指向尾节点，但是尾节点未打印
        print(cur.elem)

    def add(self, item):
        """头插法。"""
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            while cur.next is not self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head
            self.__head = node

    def append(self, item):
        """尾插法。"""
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            while cur.next is not self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self, pos, item):
        count = 0
        pre = self.__head
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            while count < pos - 1:
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点。"""
        # 判空
        if self.is_empty():
            return

        cur = self.__head
        pre = None
        while cur.next is not self.__head:
            if cur.elem == item:
                if cur is self.__head:
                    # 头节点
                    # 找尾节点
                    tail = self.__head
                    while tail.next is not self.__head:
                        tail = tail.next
                    self.__head = cur.next
                    tail.next = self.__head
                else:
                    # 中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环，cur 指向尾节点
        # 或者只有一个节点
        if cur.elem == item:
            if cur is self.__head:
                # 只有一个节点
                self.__head = None
            else:
                pre.next = cur.next


    def search(self, item):
        cur = self.__head
        if self.is_empty():
            return False
        while cur.elem != item:
            if cur.next is self.__head:
                return False
            cur = cur.next
        return True
