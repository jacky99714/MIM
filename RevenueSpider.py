# -*- coding: utf-8 -*-
import requests
from lxml import etree


class RevenueInfo:
    """營收pojo"""

    def __init__(self, year, month, stockSymbol, revenue):
        year = int(year)
        if year < 1990:
            year += 1911
        self.year = str(year).strip()
        self.month = str(month).strip()
        self.stockSymbol = str(stockSymbol).strip()
        self.revenue = str(revenue).replace(",", "").strip()

    def __str__(self):
        return self.year + "/" + self.month + " : " + self.revenue


def getMothRevenueWithTenYear(stockSymbol):
    """
    取得該股近十年每月營收
    stockSymbol : 股票代碼
    """
    # print("getMothRevenueWithTenYear")
    revenueInfoList = []
    for year in range(2010, 2019, 1):
        for month in range(1, 13, 1):
            # print(str(year)+"/"+str(month))
            if(year >= 2018 and month >= 2):  # 略過當下之後的月營收
                continue
            else:
                r = getMothRevenue(stockSymbol, year, month, "otc")
                print(r)
                if(r != None):
                    revenueInfoList.append(r)

    return revenueInfoList


def getMothRevenue(stockSymbol, year, month, stockSymbolType):
    """
    取得該股月營收
    stockSymbol : 股票代碼
    year : 年
    month : 月
    stockSymbolType : otc上櫃 ;sii 上市
    """
    url = getMothRevenueUrl(year, month, "sii")
    response = requests.get(url)
    if response.status_code != 200:
        return None
    response.encoding = "big5"
    root = etree.fromstring(response.text, etree.HTMLParser())

    # tr -> td包含股票代碼(stockSymbol) -> 第三個td -> 內容
    td = root.xpath(
        "//tr[contains(td,'" + stockSymbol + "')]/td[3]/text()")
    if len(td) > 0:
        revenue = td[0]
        return RevenueInfo(year, month, stockSymbol, revenue)
    return None


def getMothRevenueUrl(year, month, stockType):
    """
    取得營收URL
    year : 民國年
    month : 月
    stockType : otc 上櫃 ; sii 上市
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
    # getMothRevenueWithTenYear("1101")
    getMothRevenue("1101", 107, 2, "sii")
    pass


if __name__ == '__main__':
    pass
