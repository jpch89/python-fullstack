def insertion_sort(li):
    n = len(li)
    # 需要选 n - 1 个元素
    for i in range(1, n):
        j = i
        while j > 0:
            if li[j] < li[j - 1]:
                li[j - 1], li[j] = li[j], li[j - 1]
            else:
                break
            j -= 1


if __name__ == '__main__':
    li = [1, 4, 2, 8, 5, 7, 3]
    print(li)
    print('-' * 20)
    insertion_sort(li)
    print(li)
"""
[1, 4, 2, 8, 5, 7, 3]
--------------------
[1, 2, 3, 4, 5, 7, 8]
"""
