# cdnScan
一个简单的爬虫脚本，实现批量识别目标是否使用了cdn服务。

基于"站长之家"的多地ping功能服务，利用爬虫实现批量识别使用了CDN的站点。

# 环境初始化

步骤一： 下载谷歌浏览器以及对应版本的驱动(https://sites.google.com/a/chromium.org/chromedriver/downloads) 或者下载云盘链接(https://cloud.189.cn/t/3UFBbqaEnQBn (访问码:xlt7))

步骤二： 解压压缩包，将目录\Chrome\Application配置到系统环境变量；并将chromedriver.exe文件放置python3目录下；配置成功后，当CMD输入google-chrome可开启谷歌浏览器。

步骤三：pip3 install requirements

使用方法：在targets.txt文件，逐行输入需要检测的域名，然后运行cdnScan.py即可。
