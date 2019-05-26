import time
import threading   # 引入 多线程 的包threading

num = 100

def test1(temp):    # temp 是Thread 中传入的参数args
    global num  # 加global可以改变全局变量
    print(temp)
    for i in range(8):
        print("------test1--------%d" %num)
        time.sleep(1)     # sleep函数 延迟一秒
        num += 1    
    print("___test1 end___")
    
    # 如果创建Thread是执行的函数，运行结束那么意味着这个子线程结束

def test2():
    for i in range(5):
        print("-------test2------ %d" %num)   
          
        # 两个线程中的全局变量是共享的

        time.sleep(1)
    print("___test2 end___")
g_nums = [11, 22]

def main():
    # target 指定将来这个线程去哪个函数
    # args 指定 传递的参数
    t1 = threading.Thread(target = test1, args=(g_nums,))   # args传入的是元组
    t2 = threading.Thread(target = test2)
    t1.start()  
    t2.start()   # start()执行 创建一个子线程跑上面的函数

    while True:
        print(threading.enumerate())   # enumerate() 的作用是获取现在所有的线程
        if len(threading.enumerate()) <= 1:
            break      # 当只剩下主线程后，跳出循环
        time.sleep(1)

if __name__ == "__main__":
    main()
