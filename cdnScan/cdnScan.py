from selenium import webdriver
from bs4 import BeautifulSoup
import time
from queue import Queue
import threading

class cdnScan(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue
    def run(self):
        while not self._queue.empty():
            host = self._queue.get()
            try:
                options = webdriver.ChromeOptions()
                options.add_argument(
                    'user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')
                driver = webdriver.Chrome(chrome_options=options)
                driver.get('http://mping.chinaz.com/Ping/SpeedTest/?host={}'.format(host))
                time.sleep(15)
                bf = BeautifulSoup(driver.page_source, 'lxml')
                driver.quit()
                result = bf.find_all('div', class_='wt-mian mt0')
                result = result[0].find_all('a')
                check_ip = result[0].string
                for i in range(num):
                    ip = result[i].string
                    if ip != check_ip:
                        print('[+]目标({})使用了CDN服务！\n'.format(host))
                        break
                    elif i == (num - 1):
                        print('[-]目标({})没用CDN服务！\n'.format(host))
                    else:
                        pass
            except:
                print('[-]连接异常!')

def getTargets():
    queue = Queue()
    with open('targets.txt', 'r') as f:
        for i in f:
            host = i.rstrip('\n')
            queue.put(host)
    threads = []
    thread_count = 5
    for i in range(thread_count):
        threads.append(cdnScan(queue))
    for t in threads:
        t.start()
    for t in threads:
        t.join()

getTargets()