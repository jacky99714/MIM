import requests
import RevenueSpider


def sentGoogleSheet(stockSymbol, stockSymbolType):
    """
    取得該股近十年每月營收
    stockSymbol : 股票代碼
    stockSymbolType: otc上櫃 sii 上市
    """
    revenueInfos = RevenueSpider.getMothRevenueWithTenYear(
        stockSymbol, stockSymbolType)
    revenueFormat = revenueInfoDataFormat(revenueInfos)

    url = "https://script.google.com/macros/s/AKfycbyjODcLO3-5jIqgkCy83fi9NZLz8kL_wRAT2CixKFA4/exec"
    data = {
        "sheetUrl": "https://docs.google.com/spreadsheets/d/1wOt1WAQ6puQAK63fHMpCS1D34wWvWqCqM_odNmqFW_U/edit#gid=0",
        "sheetTag": stockSymbol,
        "action": "write",
        "data": ";".join(revenueFormat)
    }
    r = requests.get(url, params=data)


def revenueInfoDataFormat(revenueInfos):

    resultdict = {}

    years = set(map(lambda x: x.year, revenueInfos))

    for year in years:
        print(year)
        datas = filter(lambda x: x.year == year, revenueInfos)
        for data in datas:
            if(resultdict.get(year, None) == None):
                resultdict[year] = [data.revenue]
            else:
                resultdict[year].append(data.revenue)

    result = []
    for year in resultdict.keys():
        result.append(year+","+",".join(resultdict[year]))

    return result


if __name__ == "__main__":
    sentGoogleSheet("1526", "sii")
