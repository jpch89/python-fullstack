def print_info(name, title='', gender=True):
    """

    :param title: 职位
    :param name: 班上同学的姓名
    :param gender: True 男生 False 女生
    :return:
    """

    gender_text = '男生'
    if not gender:
        gender_text = '女生'
    # 这里其实可以用if else的三元表达式
    # gender_text = '男生' if gender else '女生'

    print('[%s]%s 是 %s' % (title, name, gender_text))


# 假设：班上的同学，男生居多！
# 提示：在指定缺省参数的默认值时，应该使用最常见的值作为默认值！
print_info('小明')
print_info('老王')
print_info('小美', gender=False)
# 如果按顺序指定关键字参数（缺省参数），是不用指定参数名的
# print_info('小美', '老师', False)
