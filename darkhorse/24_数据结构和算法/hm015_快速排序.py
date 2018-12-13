def quick_sort(li, first, last):
    """快速排序"""
    if first >= last:
        return

    pivot = li[first]
    low = first
    high = last

    while low < high:
        # high 左移
        while low < high and li[high] >= pivot:
            high -= 1
        li[low] = li[high]

        # low 右移
        while low < high and li[low] < pivot:
            low += 1
        li[high] = li[low]

    # 从循环退出时，low == high
    li[low] = pivot
    quick_sort(li, first, low - 1)
    quick_sort(li, low + 1, last)


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    print('-' * 40)
    quick_sort(li, 0, len(li) - 1)
    print(li)

"""
[54, 26, 93, 17, 77, 31, 44, 55, 20]
----------------------------------------
[17, 20, 26, 31, 44, 54, 55, 77, 93]
"""
