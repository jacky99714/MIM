import requests
import RevenueSpider


def sentGoogleSheet(stockSymbol, stockSymbolType, isOutCounty=0):
    """
    取得該股近十年每月營收
    stockSymbol : 股票代碼
    stockSymbolType: otc上櫃 sii 上市
    """
    revenueInfos = RevenueSpider.getMothRevenueWithTenYear(
        stockSymbol, stockSymbolType, isOutCounty)
    revenueFormat = revenueInfoDataFormat(revenueInfos)

    url = "https://script.google.com/macros/s/AKfycbyjODcLO3-5jIqgkCy83fi9NZLz8kL_wRAT2CixKFA4/exec"
    data = {
        "sheetUrl": "https://docs.google.com/spreadsheets/d/1wOt1WAQ6puQAK63fHMpCS1D34wWvWqCqM_odNmqFW_U/edit#gid=0",
        "sheetTag": stockSymbol,
        "action": "write",
        "data": str(revenueFormat).replace("\'", "\"")
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

    revenueInfoForYear1 = []
    for year in resultdict.keys():
        revenueInfoForYear1.append(year+"#"+"#".join(resultdict[year]))

    result = {
        "revenueInfoForYear": "%".join(revenueInfoForYear1),
        "name": revenueInfos[0].stockName
    }
    return result


if __name__ == "__main__":

    # sentGoogleSheet("1526", "sii")
    # sentGoogleSheet("6150", "otc")
    # sentGoogleSheet("8924", "otc")
    # sentGoogleSheet("5281", "otc", 1)
    # sentGoogleSheet("3611", "otc")
    # sentGoogleSheet("8358", "otc")
    # sentGoogleSheet("3339", "otc")
