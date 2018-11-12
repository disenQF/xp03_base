import random
from multiprocessing import Process, Queue
from threading import Thread, current_thread
# from queue import Queue  # 多线程的队列
import ssl

from urllib.request import urlretrieve
import os

import time

ssl._create_default_https_context = ssl._create_unverified_context

def download(url: str):
    print(current_thread().name, '开始下载', url)
    dirname = 'files'
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    if url.endswith('/'):
        filename = 'index.html'
    else:
        filename = url.split('/')[-1]

    urlretrieve(url, os.path.join(dirname, filename))


def request(queue):
    # 从队列中读取url
    # 并启动线程下载url
    while True:
        try:
            url = queue.get(timeout=10)
            # 异步操作
            Thread(target=download, args=(url, )).start()
        except: break

    print('--request over--')


if __name__ == '__main__':
    urls = ('http://www.baidu.com/',
            'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3983926072,267415974&fm=111&gp=0.jpg',
            'https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1419051179,3849014730&fm=27&gp=0.jpg',
            'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=792227929,2145243941&fm=111&gp=0.jpg')

    queue = Queue(maxsize=100)

    reqProcess = Process(target=request, args=(queue, ))
    reqProcess.start()

    for url in urls:
        time.sleep(random.randint(1, 5))
        queue.put(url)

    reqProcess.join()
    print('--All Over--')


