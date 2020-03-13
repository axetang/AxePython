'''
Day 22：Python 多线程和协程 6 方面使用逻辑通俗易懂总结
一般地，一个程序或者一个 App，默认只在一个进程的一个线程中执行，
这个线程称为主线程。如果需要开启至少另外一个线程做任务，那么就要用到今天的知识——多线程，及高效的协程技术。
首先，导入线程相关的模块 threading：
    import threading
'''
import threading
# threading 的方法 current_thread() 返回当前线程：
t = threading.current_thread()
print(t)
# t.getName() 获得这个线程的名字；其他常用方法，
# getName() 获得线程 id，isAlive() 判断线程是否存活。
print(t.getName())
print(t.isAlive())
print(t.ident)


def print_i(i):
    print('打印i:%d' % (i,))
    t = threading.current_thread()
    print(t.getName())
    print(t.ident)
    print(t.isAlive())


my_thread = threading.Thread(name='Axe Thread', target=print_i, args=(1,))
my_thread.start()
