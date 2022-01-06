#https://itchat.readthedocs.io/zh/latest/
import time
import itchat
from apscheduler.schedulers.blocking import BlockingScheduler


def send_news():
    my_friend = itchat.search_friends(name=u'文件传输助手')


if __name__ == '__main__':
    itchat.auto_login()
    itchat.send('Hello, filehelper', toUserName='filehelper')
