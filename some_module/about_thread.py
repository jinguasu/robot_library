# -*- coding: utf-8 -*-
# http://blog.csdn.net/cain/article/details/6605705  参考

import threading, time

def a(tjoin):
    print('i am running')

    tjoin.start()

    tjoin.join() # 此时，不会直接运行下一步，而要等待tjoin里所有的数据打印完，即这个线程结束才可以继续下面的线程

    print('i can end')

def b(num):
    for i in range(0,int(num)):
        print('yeah')

tjoin = threading.Thread(target=b,args=(3,))
c = threading.Thread(target=a,args=(tjoin,))

#c.start()


#data = 0
lock = threading.Lock()

def func1():
    global data   #  这里声明的意思是你要想一个全局变量赋值，而不是简单的使用，全局变量在赋值前要先声明一下
    print('%s is requiring lock' %threading.currentThread().getName())
    if lock.acquire():
        print('%s have get the lock' %threading.currentThread().getName())
        data = data + 1
        print(data)
        time.sleep(2)
        print('%s release lock'%threading.currentThread().getName())
        lock.release()


#t1 = threading.Thread(target=func1,args=())
#t2 = threading.Thread(target=func1,args=())
#t3 = threading.Thread(target=func1,args=())

#t1.start()
#t2.start()
#t3.start()


rlock = threading.RLock()

def func2():
    print('%s is require lock'%threading.currentThread().getName())
    if rlock.acquire():
        print('%s has get the lock'%threading.currentThread().getName())
        time.sleep(2)
        print('%s is require lock again' % threading.currentThread().getName())
        if rlock.acquire():
            print('%s get the lock again' % threading.currentThread().getName())
            time.sleep(2)
        print('%s is release lock' % threading.currentThread().getName())
        rlock.release()
        time.sleep(2)

        print('%s is release lock again' % threading.currentThread().getName())
        rlock.release()

#t1 = threading.Thread(target=func2,args=())
#t2 = threading.Thread(target=func2,args=())
#t3 = threading.Thread(target=func2,args=())

#t1.start()
#t2.start()
#t3.start()



product = None

#con = threading.Condition()

def produce():
    global product
    #print('%s is require lock' % threading.currentThread().getName())
    if con.acquire():
        print('%s get lock' % threading.currentThread().getName())
        while True:
            if product is None:
                print('priduce....')
                product = 'everything'
                #time.sleep(5)
                con.notify()   # 通知另一个线程，你可以开始进入锁定池等待锁定

                con.wait()   #是本县城进去等待池等待通知并且释放锁
                print('%s is release lock' % threading.currentThread().getName())
                time.sleep(2)

def consumer():
    global product
    #print('%s is require lock' % threading.currentThread().getName())
    if con.acquire():
        print('%s is get lock' % threading.currentThread().getName())
        while True:
            if product is not None:
                print('consume')
                product = None

                con.notify()   #通知另一个线程，你可以开始进入锁定池子了

                con.wait()
                print('%s is release lock' % threading.currentThread().getName())
                time.sleep(2)

#t1 = threading.Thread(target=produce)
#t2 = threading.Thread(target=consumer)
#t1.start()
#t2.start()


con = threading.Condition()
l = None

def creat_list():
    global l
    if con.acquire():        #此线程获得锁
        print('%s is get lock' % threading.currentThread().getName())
        l = []        #创建list
        print('list has been made, will notify other thread to write...')
        con.notify()
        #con.wait()    不用等待通知，因为任务已经完成
        con.release()


def write_1():
    #global l
    if con.acquire():
        print('%s is get lock' % threading.currentThread().getName())
        for i in range(5):
            l.append(1)
            print(l)
            con.notify()   #通知另一个线程
            con.wait()    #等待写完2来通知
            time.sleep(1)


def write_2():
    #global l
    if con.acquire():    #  同步阻塞
        print('%s is get lock' % threading.currentThread().getName())
        for i in range(5):
            l.append(2)
            print(l)
            con.notify()
            con.wait()   #  条件阻塞
            time.sleep(1)

t1 = threading.Thread(target=creat_list)
t2 = threading.Thread(target=write_1)
t3 = threading.Thread(target=write_2)
t1.start()
t2.start()
t3.start()

from multiprocessing import Process
from multiprocessing import Pool
import subprocess
import os,time,random

def run_proc(name):
    print('this child process %s is running with pidID is %s' %(name,os.getpid()))
    time.sleep(2)
#if __name__ == '__main__':
    #print('parent process is %s' %os.getpid())
    #p = Process(target=run_proc,args=('test',))
    #p.start()
    #p.join()
    #print('child is end')






# -*- coding: utf-8 -*-

import threading,time

def a(x):
    time.sleep(3)
    print 2+int(x)


t1 = threading.Thread(target=a,args='4',name='sun')


t1.start()

t1.ident   #   获取线程的标识符，只有在start后才会有

t1.join(2)   #表示阻塞主调线程，就是这个程序的主体，如果不执行完就不会打印下面的数字，这里设置超时2秒，2秒后就会打印下面的数字，但是这时a函数还没运行完，所以后来会打印出来。

print 234234






















