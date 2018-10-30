from distutils.core import setup

# 字典参数/关键字参数
setup(name="hm_message",  # 包名
      version="1.0",  # 版本
      description="jpch89's 发送和接收消息模块",  # 描述信息
      long_description="完整的发送和接收消息模块",  # 完整描述信息
      author="jpch89",  # 作者
      author_email="jpch89@outlook.com",  # 作者邮箱
      url="www.jpch89.com",  # 主页
      py_modules=["hm_message.send_message",
                  "hm_message.receive_message"])
