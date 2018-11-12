from multiprocessing import Process, Pipe,current_process

import time

name = 'disen'
age = 20


def printer(conn):
    global name, age  # 复制主进程的name和age到子进程中
    print(name, age)
    name = 'jack'
    age = 30
    print(current_process().name,'等待接收任务')
    msg = conn.recv()
    print(current_process().name, '--->', msg)
    print(name, age)


if __name__ == '__main__':
    conn1, conn2 = Pipe(False)  # 半双工， conn1 只收， conn2 只发

    p = Process(target=printer, args=(conn1, ))
    p.start()
    time.sleep(10)
    conn2.send('我要打印图片....')
    p.join()
    print(name, age)  # 不受子进程的影响
    print('---Over---')
