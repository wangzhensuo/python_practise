# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = '强子'
import os
import PIL,numpy
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
from subprocess import run

need_update = True

def get_screen_image():
    #run("del screen.png",shell=True)
    run('adb shell screencap -p /sdcard/1/screen.png',shell=True)#获取当前界面的手机截图
    run('adb pull /sdcard/1/screen.png',shell=True)#下载当前这个截图到当前电脑当前文件夹下
    #os.system('adb shell rm /sdcard/1/screen.png',shell=True)
    #os.system('adb shell rm /sdcard/1/screen.png')
    return numpy.array(PIL.Image.open('screen.png'))

def jump_to_next(point1, point2):#计算炫的长度
    x1, y1 = point1; x2, y2 = point2
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    run('adb shell input swipe 320 410 320 410 {}'.format(int(distance*2.09)),shell=True)
    #os.system('del screen.png')

def on_calck(event, coor=[]):#绑定的鼠标单击事件
    global need_update
    coor.append((event.xdata, event.ydata))
    if len(coor) == 2:
        jump_to_next(coor.pop(), coor.pop())
    need_update = True

def update_screen(frame):#更新图片 /从画图片
    global need_update,axes_image
    if 1:#need_update:
        time.sleep(1)
        axes_image.set_array(get_screen_image())
        need_update = False
    return axes_image,

figure = plt.figure()#创建一个空白的图片对象/创建一张图片
axes_image = plt.imshow(get_screen_image(), animated=True)#把获取的图片话在坐标轴上面
figure.canvas.mpl_connect('button_press_event', on_calck)
ani = FuncAnimation(figure, update_screen, interval=100, blit=True)
plt.show()
