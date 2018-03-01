import requests


def getInfo(stocksymbol):
    url = "http://jsjustweb.jihsun.com.tw/z/zc/zch/zch_1526.djhtm"
    response = requests.get(url)
    print(response.encoding)
    response.encoding = "big5"
    root = etree.fromstring(response.text, etree.HTMLParser())

    print(response.content)


def main():
    getInfo("1526")
    pass


if __name__ == '__main__':
    main()
