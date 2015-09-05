import json
import urllib.request

VERSION = "1"
PAGE = "1"
COUNT = "10"
appKey = "your_appKey"


def weather_caller():
    version = VERSION
    lat = str(37.3418599)
    lon = str(126.8312599)

    url = "http://apis.skplanetx.com/weather/summary?version="+version+"&lat="+lat+"&lon="+lon

    req = urllib.request.Request(url)
    req.add_header("appKey", appKey)
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')

    data = json.loads(result)
    weather = data['weather']
    weather_dict = weather['summary']
    weather_list = weather_dict[0]
    return weather_list


def search_caller(data, string_data):
    url = api_setting(data)
    url += ("&searchKeyword=" + string_data)
    req = urllib.request.Request(url)
    req.add_header("appKey", appKey)
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')

    data = json.loads(result)
    search_data = data['melon']

    return search_data


def song_caller():
    version = VERSION
    page = PAGE
    count = COUNT

    url = "http://apis.skplanetx.com/melon/charts/realtime?version=" + version + "&page=" + page + "&count=" + count

    req = urllib.request.Request(url)
    req.add_header("appKey", appKey)
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')

    data = json.loads(result)
    melon_obj = data['melon']

    return melon_obj


def api_setting(data):
    version = VERSION
    page = PAGE
    count = COUNT

    if data == "album_search":
        url = "http://apis.skplanetx.com/melon/albums?version=" + version + "&page=" + page + "&count=" + count
    elif data == "artist_search":
        url = "http://apis.skplanetx.com/melon/artists?version=" + version + "&page=" + page + "&count=" + count
    else:
        url = "http://apis.skplanetx.com/melon/songs?version=" + version + "&page=" + page + "&count=" + count

    return url
