import time
import threading
g_num = 0
def test1(num):   
    global g_num 
    # 上锁，如果之前没有被上锁，那么此时上锁成功
    # 如果已被上锁就会堵塞在这里，直到上锁成功
    mutex.acquire()
    for i in range(num):
        g_num += 1 
    # 解锁
    mutex.release()
    print("-----in test1 g_num = %d" %g_num)
    

def test2(num):
    global g_num
    mutex.acquire()  # 上锁也可以放到for中，上锁的代码越少越好
    for i in range(num): 
        g_num += 1
    print("-----in test2 g_num = %d" %g_num)
    mutex.release()

# 创建一个互斥锁，默认是没有上锁的
mutex = threading.Lock()

def main():
    t1 = threading.Thread(target = test1, args=(1000000,))   
    t2 = threading.Thread(target = test2, args=(1000000,))  
    # 多进程在共同工作时，会出现资源竞争的情况，会出错
    t1.start()  
    t2.start()   

    time.sleep(5)

    print("----- g_num = %d-----" %g_num)



if __name__ == "__main__":
    main()
