from PIL import Image
#使用第三方库：Pillow
import math
import operator
from functools import reduce
import cv2
from subprocess import run
import time
def picCompare(picA,picB):
    image1=Image.open(picA)
    image3=Image.open(picB)
    #把图像对象转换为直方图数据，存在list h1、h2 中
    h1=image1.histogram()
    image1=image3.histogram()
    print(h1)
    time.sleep(10)
    result = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
    '''
    sqrt:计算平方根，reduce函数：前一次调用的结果和sequence的下一个元素传递给operator.add
    operator.add(x,y)对应表达式：x+y
    这个函数是方差的数学公式：S^2= ∑(X-Y) ^2 / (n-1)
    '''
    print(result)
    if result>200:
        return True
    else:
        return False

vc = cv2.VideoCapture('A.flv') #读入视频文件  
  
if vc.isOpened(): #判断是否正常打开  
    rval , frame = vc.read()  
else:  
    rval = False  
c=1
timeF = 125  #视频帧计数间隔频率  
oldJPG = 'tmp.jpg'
name = 0
while rval:   #循环读取视频帧
    rval, frame = vc.read()
    if(c%timeF == 0): #每隔timeF帧进行存储操作
        cv2.imwrite('new.jpg',frame) #存储为图像
        if(picCompare('new.jpg',oldJPG)):
            name = name + 1
            run('copy new.jpg '+oldJPG,shell=True)
            run('move new.jpg '+'image/'+str(name)+'.jpg',shell=True)
            cv2.imwrite(oldJPG,frame) #存储为图像
    c = c + 1
    cv2.waitKey(1)  
vc.release()  
