info_tuple = ('小明', 18, 1.75)

# 格式化字符串后面的 () 本质上就是元组
print('%s 年龄是 %d 身高是 %.2f' % info_tuple)

# 使用格式化字符串和元组来拼接一个新的字符串
info_str = '%s 年龄是 %d 身高是 %.2f' % info_tuple

print(info_str)
