def selection_sort(li):
    n = len(li)
    for i in range(n - 1):
        min_i = i
        for j in range(i + 1, n):  # j: 0 ~ n - 2
            if li[j] < li[min_i]:
                min_i = j
        li[i], li[min_i] = li[min_i], li[i]

if __name__ == '__main__':
    li = [1, 4, 2, 8, 5, 7, 3]
    print(li)
    print('-' * 20)
    selection_sort(li)
    print(li)
"""
[1, 4, 2, 8, 5, 7, 3]
--------------------
[1, 2, 3, 4, 5, 7, 8]
"""
