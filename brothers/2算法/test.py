class Message:
    def __init__(self):
        self.val = ['大', '王', '叫', '我', '来', '巡', '山']

    def __getitem__(self, i):
        print('我是 __getitem__')
        return self.val[i]

    # def __iter__(self):
    #     print('我是 __iter__')
    #     return iter(self.val)


msg = Message()
for i in msg:
    print(i)
