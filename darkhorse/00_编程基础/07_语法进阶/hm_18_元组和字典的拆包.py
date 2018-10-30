def demo(*args, **kwargs):
    print(args)
    print(kwargs)


# 元组变量/字典变量
gl_nums = (1, 2, 3)
gl_dict = {'name': '小明', 'age': 18}

# demo(gl_nums, gl_dict)
demo(*gl_nums, **gl_dict)

# 为什么叫做拆包？
# 如果不使用拆包：
# demo(1, 2, 3, name='小明', age=18)
# 拆包语法可以简化元组/字典变量的传递
