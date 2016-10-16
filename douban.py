# -*- coding:utf-8 -*-

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from urllib.request import urlopen
import re, threading


def douban(ID):
    varl.set('已经获取%s页' % (ID / 20))
    html = urlopen(
        'https://read.douban.com/tag/%E7%9F%AD%E7%AF%87%E5%B0%8F%E8%AF%B4/?cat=article&sort=top&start=' + str(ID))
    sd = html.read()
    # print sd
    reg = r'<span class="price-tag ">(.*?)元</span>.*?\'read.douban.com\'\)">(.*?)</a>'
    reg = re.compile(reg)
    return re.findall(reg, sd)


# print q


def write():
    ID = 0
    a = []
    b = 0
    while ID <= 440:
        List = douban(ID)
        ID += 20
        for i in List:
            b += 1
            a.append(float(i[0]))
            text.insert(END, '书名:%s    价格:￥%s\n' % (i[1], i[0]))
        # time.sleep(0.5)
    text.insert(END, '-------------------------------------------------\n')
    text.insert(END, '该分类书本总数量:%s\n' % b)
    text.insert(END, '书本总价格:%s\n' % sum(a))
    text.insert(END, '平均每本￥%f' % (sum(a) / b))
    varl.set('全部处理完成')


def qidoong():
    t1 = threading.Thread(target=write)
    t1.start()


root = Tk()
root.title('漠北老师的GUI软件')
root.geometry('660x560+500+200')
root.resizable(width=False, height=False)

text = ScrolledText(root, font=('微软雅黑', 10))
text.grid()

a = Button(root, text='开始分析', font=('微软雅黑', 21), command=qidoong)
a.grid()

varl = StringVar()

b = Label(root, fg='blue', textvariable=varl)
b.grid()
varl.set('准备中.....')

root.mainloop()
