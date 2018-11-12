from multiprocessing import Process, current_process

import time


class Downloader(Process):
    def __init__(self, url, headers):
        super().__init__()
        self.url = url
        self.headers = headers

    def run(self):
        print(self.name, '开始下载', self.url)
        print(self.headers)
        time.sleep(2)
        print(self.url, '下载完成')


if __name__ == '__main__':
    headers = {
        'Content-Type': 'application/json;charset=utf-8',
        'Host': 'jd.com',
        'User-Agent': 'Spider'
    }
    urls = ('http://www.baidu.com', 'http://www.jd.com', 'http://www.hao123.com')

    downloads = [Downloader(url, headers) for url in urls]

    for download in downloads:
        download.start()

    for download in downloads:
        download.join()

    print('---over---')
