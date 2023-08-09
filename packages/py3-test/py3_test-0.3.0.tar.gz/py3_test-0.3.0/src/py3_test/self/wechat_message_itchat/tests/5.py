"""
@Time   : 2019/5/20
@author : lijc210@163.com
@Desc:  : 功能描述。
"""
import itchat
from itchat.content import CARD, MAP, NOTE, SHARING, TEXT


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    print(msg)
    if msg.user.RemarkName in ["陈城", "谢彦彬"] or msg.user.NickName in ["陈城", "谢彦彬"]:
        print("aaaaaa")
        msg.user.send("{}: {}".format(msg.type, msg.text))


itchat.auto_login(True)
print(itchat.get_friends())
print(itchat.get_chatrooms())
print(itchat.get_contact())

itchat.run(True)
