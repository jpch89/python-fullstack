msg = input()
while msg != '退出':
    msg = msg.replace('吗', '')
    msg = msg.replace('?', '!')
    msg = msg.replace('？', '！')
    print(msg)
    msg = input()
