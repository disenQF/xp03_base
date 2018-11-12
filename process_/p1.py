from multiprocessing import Process, current_process
import time
import random


def download(url, headers):
    print(current_process().name, '开始下载', url)
    print(headers)
    time.sleep(random.randint(1, 5))

    print(url, '下载完成')


if __name__ == '__main__':  # 当前脚本作为程序的入口时，__name__就是"__main__"
    # 类似于 c或java的main()函数,
    url = 'http://www.baidu.com/'
    headers = {
        'Content-Type': 'text/html;charset=utf-8',
        'Referer': 'https://home.firefoxchina.cn/'
    }
    p = Process(target=download, kwargs={'url': url,
                                         'headers': headers})
    p.start()
    p.join()  # 等待子进程结束
    print('--over--')
