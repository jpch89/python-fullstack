class Node:
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SinglyLinkedList:
    """单链表"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        # return True if self.__head is None else False
        # 推荐写法：
        return self.__head is None

    def length(self):
        """链表长度"""
        # cur 游标，用来移动遍历节点
        cur = self.__head
        # count 记录数量
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
        """链表头部添加元素，头插法。"""
        node = Node(item)
        self.__head, node.next = node, self.__head
        # 如果采用下面这种写法，要注意顺序！
        # node.next = self.__head
        # self.__head = node

    def append(self, item):
        """链表尾部添加元素，尾插法。"""
        # 注意这个 item 不是节点对象，而是数据
        # 所以要新建一个节点
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
            return
        while cur.next:
            cur = cur.next
        cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素
        :param pos 从 0 开始
        """
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                pre = pre.next
            # 当循环退出后，pre 指向 pos - 1 位置
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur:
            if cur.elem == item:
                # 先判断此节点是否是头节点
                # 两种方式
                # pre 是 None 或者 cur 是 self.__head
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next


    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

if __name__ == '__main__':
    sll = SinglyLinkedList()
    print(sll.is_empty())
    print(sll.length())

    sll.append(1)
    print(sll.is_empty())
    print(sll.length())

    sll.append(2)
    sll.add(8)
    sll.append(3)
    sll.append(4)
    sll.append(5)
    sll.append(6)
    # 8 1 2 3 4 5 6
    sll.insert(-1, 9)  # 9 8 1 2 3 4 5 6
    sll.travel()

    sll.insert(2, 100)  # 9 8 100 1 2 3 4 5 6
    sll.travel()

    sll.insert(10, 200)  # 9 8 100 1 2 3 4 5 6 200
    sll.travel()

    sll.remove(100)
    sll.travel()

    sll.remove(9)
    sll.travel()

    sll.remove(200)
    sll.travel()

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
