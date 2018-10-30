def sum_numbers(*args):
    num = 0
    print(args)
    num = sum(args)

    # 或者采用循环遍历累加
    # for n in args:
    #     num += n

    return num


result = sum_numbers(1, 2, 3, 4, 5)
# 如果不用*args，使用元组接收函数，不是很直观
# 因为会有两个括号
# result = sum_numbers((1, 2, 3, 4, 5))
print(result)
