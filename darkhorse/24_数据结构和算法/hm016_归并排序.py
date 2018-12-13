def merge_sort(li):
    """归并排序"""
    n = len(li)
    if n <= 1:
        return li
    mid = n // 2

    left_li = merge_sort(li[:mid])
    right_li = merge_sort(li[mid:])

    left_pointer, right_pointer = 0, 0
    result = []

    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1

    result += left_li[left_pointer:]
    result += right_li[right_pointer:]

    return result

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    print('-' * 40)
    li = merge_sort(li)
    print(li)

"""
[54, 26, 93, 17, 77, 31, 44, 55, 20]
----------------------------------------
[17, 20, 26, 31, 44, 54, 55, 77, 93]
"""
