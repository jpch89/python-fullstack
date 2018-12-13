# 外层循环控制要走多少次
# 内层循环控制从头走到尾

def bubble_sort(li):
    n = len(li)
    # 冒泡 n - 1 次
    for i in range(n - 1):
        count = 0
        # 每次比较 n - i 次
        for j in range(n - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                count += 1
        # 如果某次冒泡过程中没有发生交换，则全部有序
        # 直接返回
        if count == 0:
            return

if __name__ == '__main__':
    li = [1, 4, 2, 8, 5, 7, 3]
    print(li)
    print('-' * 20)
    bubble_sort(li)
    print(li)
"""
[1, 4, 2, 8, 5, 7, 3]
--------------------
[1, 2, 3, 4, 5, 7, 8]
"""
