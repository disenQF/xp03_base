import os
import time

print('---fork 将当前程序复制到子进程中---')

pid = os.fork()  # 仅linux可用
if pid == 0:
    time.sleep(2)
    print('子进程:', os.getpid())
else:
    print('父进程', os.getpid())
    os.wait()  # 等待子程运行完成
    print('父进程结束')

# print('当前进程:', os.getpid(), '父进程：', os.getppid())  # ? 会执行几次？
