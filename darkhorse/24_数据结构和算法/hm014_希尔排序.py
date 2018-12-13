def shell_sort(li):
    """希尔排序"""
    n = len(li)
    gap = n // 2
    while gap:  # 我的写法，比较简洁
        # 控制步长的缩短
        for j in range(gap, n):
            # 插入算法，与普通插入算法的区别就是 gap 步长
            i = j
            while i > 0:
                if li[i] < li[i - gap]:
                    li[i], li[i - gap] = li[i - gap], li[i]
                else:
                    break
                i -= gap
        # 缩短 gap 步长
        gap = gap // 2

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(alist)
print(alist)
"""
[17, 20, 26, 31, 44, 54, 55, 77, 93]
"""
