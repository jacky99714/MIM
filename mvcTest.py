import requests


def sentGoogleSheet(messageText):
    r = requests.get(
        "https://script.google.com/macros/s/AKfycbyjODcLO3-5jIqgkCy83fi9NZLz8kL_wRAT2CixKFA4/exec?data="+messageText+",rr,rrr&sheetUrl=https://docs.google.com/spreadsheets/d/1wOt1WAQ6puQAK63fHMpCS1D34wWvWqCqM_odNmqFW_U/edit&sheetTag=sheet1")


if __name__ == "__main__":
    sentGoogleSheet("eee")
