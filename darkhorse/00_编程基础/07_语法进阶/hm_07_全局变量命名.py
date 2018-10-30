# 注意：在开发时，应该把模块中的所有全局变量定义在所有函数上方
# 就可以保证所有的函数都能正常访问到每一个全局变量
gl_num = 10
# 再定义一个全局变量
gl_title = 'darkhorse'
# 再定义一个全局变量
gl_name = '小明'


def demo():
    # 如果局部变量和全局变量同名
    # PyCharm会在局部变量下方显示灰色波浪线
    num = 99
    print('%d' % num)
    print('%s' % gl_title)
    print('%s' % gl_name)


demo()
