#! /usr/bin/python


"""
多线程学习
2018年03月15日
"""

# 案例一:
import time, threading, random

content = 0

def loop():
    global content
    n = 5
    for i in range(5):
        content = content + n
        content = content - n
        print(threading.current_thread().name, content)
        time.sleep(random.randint(1,3))


thread_list = []

for index in range(10):
    t = threading.Thread(target=loop, name='LoopThread' + str(index))
    thread_list.append(t)


for item in thread_list:
    item.setDaemon(True)
    item.start()

for item in thread_list:
    item.join()
# t.join()
print(content)