from timeit import Timer


def test1():
    """使用加号拼接列表。"""
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    """使用 append 追加列表。"""
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    """使用列表推导式。"""
    l = [i for i in range(1000)]


def test4():
    """使用 list 转换可迭代对象。"""
    # Python 2 中想要得到可迭代的 range
    # 需要使用 xrange
    l = list(range(1000))


t1 = Timer('test1()', globals=globals())
t2 = Timer('test2()', globals=globals())
t3 = Timer('test3()', globals=globals())
t4 = Timer('test4()', globals=globals())

print('使用加号拼接列表：%s' % t1.timeit(number=1000))
print('使用 append 追加列表：%s' % t1.timeit(number=1000))
print('使用列表推导式：%s' % t1.timeit(number=1000))
print('使用 list 转换可迭代对象：%s' % t1.timeit(number=1000))

"""
使用加号拼接列表：1.8383459586043422
使用 append 追加列表：1.959418708009967
使用列表推导式：1.7276078443271952
使用 list 转换可迭代对象：1.6721926026145377
"""

from timeit import timeit
t = timeit('test1()', number=1000, globals=globals())
print(t)


def test5():
    """在末尾添加元素。"""
    li = []
    for i in range(1000):
        li.append(i)


def test6():
    """在头部添加元素。"""
    li = []
    for i in range(1000):
        li.insert(0, i)


print('在末尾 append：%s' % timeit('test5()', number=1000, globals=globals()))
print('在头部 insert：%s' % timeit('test6()', number=1000, globals=globals()))
"""
在末尾 append：0.08858736782733523
在头部 insert：0.5678873078543223
"""

my_li = list(range(10000))
def test7():
    """在头部取元素。"""
    head = my_li.pop(0)
print('在头部取元素：%s' % timeit('test7()', number=1000, globals=globals()))

my_li = list(range(10000))
def test8():
    """在尾部取元素。"""
    tail = my_li.pop()
print('在尾部取元素：%s' % timeit('test8()', number=1000, globals=globals()))

"""
在头部取元素：0.0030223006789800166
在尾部取元素：0.00019812512940653448
"""
