# -*- coding: utf-8 -*-

import threading,time

def a(x):
    time.sleep(3)
    print 2+int(x)


t1 = threading.Thread(target=a,args='4',name='sun')


t1.start()

t1.ident   #   获取线程的标识符，只有在start后才会有

t1.join(2)   #表示阻塞面的数字，这里设置超时2秒，2秒后就会打印下面的数字，但是这时a函数还没运行完，所以后来会打印出来。

print 234234
