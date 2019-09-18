import time
import threading

lock = threading.RLock()
n=10
# 不加锁

def task(i):
    global n
    print('这段代码加锁')
    lock.acquire()#加锁
    print('当前线程',i,'当前读取到的n',n)
    n = i
    time.sleep(1)
    print('当前线程',i,'修改后读到的n',n)
    lock.release()#释放锁


for i in range(10):
    t = threading.Thread(target=task,args=(i,))
    t.start()


