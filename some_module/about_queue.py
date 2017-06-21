import queue,threading,random,time

p = queue.Queue(maxsize=2)   #先进先出的栈， 最大是2个

w = queue.LifoQueue()  # 先进后出的堆

e = queue.PriorityQueue   #按优先级来出，等级越低先出来

p.put(10)   # 放入数据

p.put(2)

#p.put_nowait(1)

print(p.full())  # 这里是满的 所以返回true
print(p.get())   #  取出数据
print(p.get())
#print(p.get_nowait())
#print(p.get(1,2))
print(p.qsize())   #  此处为0 因为已经取出2个了，里面没有东西了
print(p.empty())   # 判断是否为空，是的话返回true

q = queue.Queue(maxsize=99)

def put_in_queue():
    for i in range(10):
        i = random.randint(1,99)
        #print(i)
        q.put(i)
        #time.sleep(1)

def get_j_num():
    j = []
    while True:
        #print(q.empty())
        try:
            i = q.get(1,5)
            if i % 2 == 1:
                #print('this mun %s is out' % i)
                j.append(i)
            else:
                q.put(i)   #发现不是想要的后要把它返还给队列
        except:    # 在5秒后还接受不到数字，即队列里还没有数据，就会异常，这里捕捉后推出while循环出来
            print(j)
            break   #  推出while循环
def get_o_num():
    o = []
    while True:
        try:
            i = q.get(1,5)
            if i % 2 == 0:
                #print('this mun %s is out'%i)
                o.append(i)
            else:
                q.put(i)
        except:
            print(o)
            break

t1 = threading.Thread(target=put_in_queue)
t2 = threading.Thread(target=get_j_num)
t3 = threading.Thread(target=get_o_num)

#t1.start()
#t2.start()
#t3.start()
#t1.join()
#t2.join()
#t3.join()
