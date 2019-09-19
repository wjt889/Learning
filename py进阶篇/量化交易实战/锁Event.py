import time
import threading


lock = threading.Event

def fun(arg):
    print("线程来了")
    lock.wait(1)  #加锁
    print(arg)

for i in range(10):
    t = threading.Thread(target=fun,args=(i,))
    t.start()

input(">>>>")
lock.set() #绿灯开锁
lock.clear()  #清除

for i in range(10):
    t1 = threading.Thread(target=fun,args=(i,))



