# -*- coding: utf-8 -*-
import requests
from lxml import etree


class RevenueInfo:
    """營收pojo"""

    def __init__(self, year, month, stockSymbol, revenue):
        year = int(year)
        if year > 1990:
            year -= 1911
        self.year = str(year).strip()
        self.month = str(month).strip()
        self.stockSymbol = str(stockSymbol).strip()
        self.revenue = str(revenue).strip()

    def __str__(self):
        return self.year + "/" + self.month + " : " + self.revenue


def getMothRevenue(stockSymbol):
    """取得該股近十年每月營收"""

    for year in range(2017, 2018, 1):
        for month in range(1, 12, 1):
            url = getMothRevenueUrl(year, month, "sii")
            response = requests.get(url)
            response.encoding = "big5"
            root = etree.fromstring(response.text, etree.HTMLParser())

            #   公司代號    公司名稱   當月營收     上月營收	去年當月營收	上月比較 增減(% )	去年同月 增減( % )	當月累計營收	去年累計營收	前期比較 增減( % )
            td = root.xpath(
                "//tr[contains(td,'"+stockSymbol+"')]/td[3]/text()")
            revenue = td[0]
            r = RevenueInfo(year, month, stockSymbol, revenue)
            print(r)


def getMothRevenueUrl(year, month, stockType):
    """
    取得營收URL
    year : 民國年
    month : 月
    type : otc 上櫃 ; sii 上市
    """
    # 假如是西元，轉成民國
    if year > 1990:
        year -= 1911

    prefix_url = 'http://mops.twse.com.tw/nas/t21/'
    type_url = stockType + "/t21sc03_"
    time_url = str(year) + "_" + str(month)
    sufffix_url = "_0.html"

    if year <= 98:
        sufffix_url = ".html"
    url = prefix_url + type_url + time_url + sufffix_url
    return url


def main():
    getMothRevenue("1101")
    pass


if __name__ == '__main__':
    main()
