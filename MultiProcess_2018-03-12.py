#!/usr/bin/python


"""
主要学习 进程 与 线程
"""

# 案例六 : 用线程池管理多进程  以及如何退出子进程

from multiprocessing import Pool
import random
import os
import time

def a(i):
    for index in range(20):
        print('print: {}, index: {}'.format(i, index))
        if random.randint(0,1) == 1:
            Pool.terminate() # 任意时候调用, 子进程结束
        time.sleep(3)

pool = Pool(8) # 超过进程池中的数量会等待前面的子进程退出后运行

for i in range(10):
    pool.apply_async(a, args=(i,)) # 通过sleep得出加入时就会执行
    time.sleep(1)
pool.close() # 关闭进程池, 禁止后续加入
pool.join()  # 主进程阻塞等待子进程退出


# 案例五 : 通过 Process -> run() 对象的访问方法实现多线程

"""
from multiprocessing import Process
import os
import time

class P(Process):
    def __init__(self, index):
        self.index = index
        super().__init__();

    def run(self):
        for i in range(2):
            print('index:{}, times: {}, PID: {}, PPID: {}'.format(self.index, i, os.getpid(), os.getppid()))
            time.sleep(2)

for index in range(10):
    p = P(index)
    p.start()
"""


# 案例四 : multiprocessing 模块实现多进程问题

"""
from multiprocessing import Process
import os
import time

def a(i):
    while True:
        print('this is sub process, {}'.format(i))
        time.sleep(5)


for i in range(10):
    p = Process(target = a, args=(i,))
    p.start()
    #exit()  # 主程序会终止后面的步骤但是不会退出
print('这里还是可以执行')
exit() # 主程序会终止后面的步骤但是不会退出
print('这句就执行不到了')
# exit()
"""
# ================

# 案例三 : 解决僵尸进程问题(使用信号方式解决)
"""
#!/usr/bin/env python  
import os,time,signal  
def chldHandler(signum,stackframe):  
    while 1:  
        try:  
            result = os.waitpid(-1,os.WNOHANG)  
        except:  
            break  
        print 'Reaped child process %d' % result[0]  
signal.signal(signal.SIGCHLD,chldHandler)  
print 'before the fork,my PID is:',os.getpid()  
pid = os.fork()  
if pid:  
    print 'Hello from the parent.The child will be PID %d' %pid  
    print 'Sleeping 10 seconds...'  
    time.sleep(10)  
    print 'Sleep done.'  
else:  
    print 'Child sleeping 5 seconds...'  
    time.sleep(5)  
"""
# 案例二 : 僵尸进程问题

"""
import os
import time

print('创建子程序前: 运行该脚本进程的PID: {} , 脚本进程的PID :{}'.format(os.getppid(), os.getpid()))

print('开始fork子程序 ...')

sub_fork = os.fork()
if sub_fork == 0:
    print('我是子程序PID:{}, 主程序的PID:{}, 我会比主进程先结束成为zombie进程,  请用ps aux| grep python 查看 '.format(os.getpid(), os.getppid()))
else:
    print('我是主程序PID:{}, 我创建子程序并先运行, 子进程会先退出并成为僵尸进程, 我先sleep(10), 主程序的PID:{}'.format(os.getpid(), os.getppid()))
    time.sleep(10)
    print('主进程sleep(10)后退出')
"""

# 案例一, 主程序创建子进程
"""
import os
import time
print('未创建子进程前只执行一次')
print('创建子程序前: 运行该脚本进程的PID: {} , 脚本进程的PID :{}'.format(os.getppid(), os.getpid()))
print('开始fork子程序 ...')
sub_fork = os.fork()
print('创建子进程后执行2次')
if sub_fork == 0:
    print('我是子程序PID:{}, 主程序的PID:{}'.format(os.getpid(), os.getppid()))
else:
    print('我是主程序PID:{}, 我创建子程序并先运行, 主程序的PID:{}'.format(os.getpid(), os.getppid()))

time.sleep(10)
"""








