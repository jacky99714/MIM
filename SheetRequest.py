import requests
import RevenueSpider
import Equipment


def sentGoogleSheet(stockSymbol, stockSymbolType, isOutCounty=0):
    revenueFormat = sentGoogleSheetRevenue(
        stockSymbol, stockSymbolType, isOutCounty)
    name = revenueFormat['name']
    print(name)

    sentGoogleSheetImformation(stockSymbol, name)


def sentGoogleSheetImformation(stockSymbol, name):

    result = Equipment.infoDataFormate(stockSymbol)

    result['name'] = name

    url = "https://script.google.com/macros/s/AKfycbyDg_HBWWJWrAspnyrrDkUNkNO6HPfgSq_7CHNlOTy9/exec"
    data = {
        "sheetUrl": "https://docs.google.com/spreadsheets/d/1wGARftMGTwvy6x4RbNUjcfUJIG6NIpZXRXqRYd3QuoQ/edit#gid=1755276593",
        "sheetTag": stockSymbol,
        "action": "write",
        "data": str(result).replace("\'", "\"")
    }
    r = requests.get(url, params=data)
    pass


def sentGoogleSheetRevenue(stockSymbol, stockSymbolType, isOutCounty=0):
    """取得該股近十年每月營收

    Arguments:
        stockSymbol {string} -- 股票代碼
        stockSymbolType {string} -- otc上櫃;sii上市

    Keyword Arguments:
        isOutCounty {int} -- 是否國外(-KY) (default: {0})
    """
    revenueInfos = RevenueSpider.getMothRevenueWithTenYear(
        stockSymbol, stockSymbolType, isOutCounty)
    revenueFormat = RevenueSpider.revenueInfoDataFormat(revenueInfos)

    url = "https://script.google.com/macros/s/AKfycbyjODcLO3-5jIqgkCy83fi9NZLz8kL_wRAT2CixKFA4/exec"
    data = {
        "sheetUrl": "https://docs.google.com/spreadsheets/d/1wOt1WAQ6puQAK63fHMpCS1D34wWvWqCqM_odNmqFW_U/edit#gid=0",
        "sheetTag": stockSymbol,
        "action": "write",
        "data": str(revenueFormat).replace("\'", "\"")
    }
    r = requests.get(url, params=data)
    return revenueFormat


if __name__ == "__main__":

    # sentGoogleSheet("1526", "sii")  # 日馳
    # sentGoogleSheet("6150", "otc")  # 撼訊
    # sentGoogleSheet("8924", "otc")  # 大田
    # sentGoogleSheet("5281", "otc", 1)  # 大峽谷
    # sentGoogleSheet("3611", "otc")  # 鼎漢
    # sentGoogleSheet("8358", "otc")  # 金居
    # sentGoogleSheet("5255", "otc")  # 美桀
    # sentGoogleSheet("1904", "sii")  # 正隆
    # sentGoogleSheet("3587", "otc")  # 閎康
    # sentGoogleSheet("4426", "sii")  # 利勤
    # sentGoogleSheet("6223", "otc")  # 旺矽
    # sentGoogleSheet("9939", "sii")  # 宏全

    # sentGoogleSheet("1229", "sii")  # 聯華
    # sentGoogleSheet("3055", "sii")  # 蔚華科
    # sentGoogleSheet("2603", "sii")  # 長榮海

    # sentGoogleSheet("3596", "sii")  # 智易
    # sentGoogleSheet("6146", "otc")  # 耕興
    # sentGoogleSheet("1476", "sii")  # 儒鴻
    # sentGoogleSheet("4807", "sii", 1)  # 日成-KY
    # sentGoogleSheet("6438", "otc")  # 迅得
    sentGoogleSheet("1597", "otc")  # 直得
