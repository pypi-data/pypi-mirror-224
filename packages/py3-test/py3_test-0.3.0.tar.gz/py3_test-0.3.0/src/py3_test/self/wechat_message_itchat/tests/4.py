"""
@Time   : 2019/5/20
@author : lijc210@163.com
@Desc:  : 功能描述。
"""
import itchat

print(itchat.check_login())
itchat.get_QRuuid()

print(itchat.load_login_status())

print(itchat.originInstance.uuid)
print(itchat.get_QR(enableCmdQR=True, picDir="QR.png", qrCallback=None))

print(itchat.load_login_status())
# @itchat.msg_register(itchat.content.TEXT)
# def text_reply(msg):
#     return msg.text
#
#
# itchat.auto_login()
# itchat.send('Hello, filehelper', toUserName='filehelper')
#
# print(itchat.check_login())
# itchat.run()
