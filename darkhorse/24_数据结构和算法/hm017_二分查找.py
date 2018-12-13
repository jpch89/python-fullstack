def binary_search1(li, item):
    """递归版本：二分查找"""
    n = len(li)
    if n > 0:
        mid = n // 2
        if li[mid] == item:
            return True
        elif item < li[mid]:
            return binary_search1(li[:mid], item)
        else:
            return binary_search1(li[mid + 1:], item)
    else:
        return False


def binary_search2(li, item):
    """非递归版本：二分查找"""
    n = len(li)
    low = 0
    high = n - 1

    while low <= high:
        mid = (high + low) // 2
        if li[mid] == item:
            return True
        elif li[mid] > item:
            high = mid - 1
        elif li[mid] < item:
            low = mid + 1

    return False


if __name__ == '__main__':
    li = [1, 2, 3, 4, 5, 7, 8, 9]
    print(binary_search1(li, 6))
    print(binary_search1(li, 3))
    print(binary_search2(li, 6))
    print(binary_search2(li, 3))

"""
False
True
False
True
"""
