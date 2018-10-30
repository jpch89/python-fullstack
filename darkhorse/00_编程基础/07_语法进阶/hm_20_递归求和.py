# 1. 定义一个函数 sum_numbers
# 2. 能够接收一个 num 的整数参数
# 3. 计算 1 + 2 + ... num 的结果


def sum_numbers(num):
    # 1. 出口
    if num == 1:
        return 1

    # 2. 数字的累加
    # 假设 sum_numbers 能够正确的处理 1 ... num-1 的累加
    temp = sum_numbers(num - 1)
    return num + temp


result = sum_numbers(3)
print(result)
