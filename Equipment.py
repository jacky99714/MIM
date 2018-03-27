# -*- coding: utf-8 -*-
import requests
from lxml import etree


def infoDataFormate(stockSymbol):

    result = []
    resultdict = {
        "result": result,
        "name": ""
    }

    getPALImformation(stockSymbol, resultdict)
    getBalanceSheet(stockSymbol, resultdict)

    resultdict['result'] = "%".join(resultdict['result'])

    return resultdict


def getPALImformation(stockSymbol, returnVal):
    """ 取得損益年表(Profit and loss chronology)資料

    Arguments:
        stockSymbol {string} -- 股票代碼
    """

    result = returnVal['result']
    root = getResponse(getUrl("損益年表", stockSymbol))

    year = root.xpath("//tr[contains(td, '年')]/child::node()/text()")
    year.insert(0, "1")
    result.append("#".join(refreshList(year)))
    # print(refreshList(year))

    # 營業收入淨額(Net operating income)
    noi = root.xpath(
        "//tr[contains(td, '營業收入淨額')]/child::node()/text()|//tr[contains(td, '營業收入淨額')]/child::node()/p/text()")
    noi.insert(0, "2")
    result.append("#".join(refreshList(noi)))
    # print(refreshList(noi))

    # 取得每股盈餘 並且移除稀釋每股盈餘
    # eps = root.xpath(
    #     "//tr[contains(td, '每股盈餘 (元)') and not(contains(td, '稀釋'))]/child::node()/text()|//tr[contains(td, '每股盈餘 (元)') and not(contains(td, '稀釋'))]/child::node()/p/text()")
    # print(eps)
    return result


def getBalanceSheet(stockSymbol, returnVal):

    result = returnVal['result']
    root = getResponse(getUrl("資產負債年表", stockSymbol))

    # year = root.xpath("//tr[contains(td, '期別')]/child::node()/text()")
    # print(refreshList(year))

    # 機器及儀器設備成本(Machinery and equipment costs)
    maec = root.xpath(
        "//tr[contains(td, '機器及儀器設備成本')]/child::node()/text()|//tr[contains(td, '機器及儀器設備成本')]/child::node()/p/text()")
    maec.insert(0, "3")
    result.append("#".join(refreshList(maec)))
    # print(refreshList(maec))

    # 未完工程及預付款(Unfinished project and advance payment)
    upaap = root.xpath(
        "//tr[contains(td, '未完工程及預付款')]/child::node()/text()|//tr[contains(td, '未完工程及預付款')]/child::node()/p/text()")
    upaap.insert(0, "5")
    result.append("#".join(refreshList(upaap)))
    # print(refreshList(upaap))

    # 其他設備成本
    omaec = root.xpath(
        "//tr[contains(td, '其他設備成本')]/child::node()/text()|//tr[contains(td, '其他設備成本')]/child::node()/p/text()")
    omaec.insert(0, "4")
    result.append("#".join(refreshList(omaec)))
    # print(refreshList(omaec))

    return result


def getResponse(url):
    """取得response

    Arguments:
        url {string} -- URL

    Returns:
        [type] -- root
    """
    response = requests.get(url)
    if response.status_code != 200:
        return None
    response.encoding = "big5"
    return etree.fromstring(response.text, etree.HTMLParser())


def getUrl(type, stockSymbol):
    """取得URL

    Arguments:
        type {string} -- 基本資料、損益年表、資產負債年表
        stockSymbol {string} --  股票代碼

    Returns:
        string -- URL
    """
    if type == "基本資料":
        return "http://jsjustweb.jihsun.com.tw/z/zc/zca/zca_"+stockSymbol+".djhtm"

    if type == "損益年表":
        return "http://jsjustweb.jihsun.com.tw/z/zc/zcq/zcqa/zcqa_"+stockSymbol+".djhtm"

    if type == "資產負債年表":
        return "http://jsjustweb.jihsun.com.tw/z/zc/zcp/zcpb/zcpb_"+stockSymbol+".djhtm"


def refreshList(list):
    """移除不需要的元素 例如：空字串、\\n、\\r

    Arguments:
        list {List} -- 陣列

    Returns:
        List -- 移除不需要元素後的List
    """
    return [x.replace(",", "") for x in list if x.replace("\n", "").replace("\r", "") != '']


if __name__ == '__main__':
    # getPALImformation("2330")
    # getBalanceSheet("2330")
    infoDataFormate("2330")
