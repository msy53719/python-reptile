import requests
from html.parser import HTMLParser


def hello(str):
    print('hello world' + str)


def gethtml(url):
    try:
        rs = requests.get(url)
        # rs.encoding = 'utf-8'
        rs.encoding = 'GBK'
        if (rs.status_code == 200):
            return rs.text
        else:
            return rs.status_code
        rs.raise_for_status
    except:
        return 'error'


def get_image(url):
    rs = requests.get(url).content
    return rs


def gethtmlheader(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.33'}
    try:
        rs = requests.get(url, headers)
        # rs.encoding = 'utf-8'
        rs.encoding = 'GBK'
        if (rs.status_code == 200):
            return rs.text
        else:
            return rs.status_code
        rs.raise_for_status
    except:
        return 'error'

# hello('python')
# 百度入口
# print(gethtml('http://www.baidu.com/s?ie=ie=utf-8&&wd=12306'))
# 网站入口
# print(gethtml('http://www.jmrenti.org/'))
# print(gethtmlheader('https://www.12306.cn/index/'))
