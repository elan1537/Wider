from flask import Flask, render_template, request
from api_caller import *
from pprint import pprint
from login import get_login, get_block

app = Flask(__name__)
app.config.from_object(__name__)

SECRET_KEY = 'miswneh8'


@app.route("/")
def main():
    get_login()
    return render_template("home.html")


@app.route("/home")
def hello_world():
    get_block()
    api = song_caller()
    return render_template('index.html', api=api)


@app.route("/weather")
def weather():
    api = weather_caller()
    location = api['grid']
    today = api['today']
    tomorrow = api['tomorrow']
    yesterday = api['yesterday']
    day_after = api['dayAfterTomorrow']
    pprint(api)
    print(location)
    print(today)
    print(tomorrow)
    print(yesterday)
    print(day_after)

    sky_case = today['sky']
    sky = sky_case['code']
    return render_template('weather.html', location=location, today=today, tomorrow=tomorrow, yesterday=yesterday, day_after=day_after)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        data = request.form['api_set']
        string_data = request.form[data]
        inform = search_return(data, string_data)
        length = len(inform)
        return render_template("search.html", inform=inform, length=length)

    return render_template("search.html")


@app.route("/song", methods=['GET', 'POST'])
def song_info():
    if request.method == 'POST':
        music_value = request.form["music_chart"]
        song = song_return(music_value)
        artist = artist_return(music_value)
        return render_template('song.html', song=song, artist=artist)

    return render_template('song.html')


def song_return(music_number):
    song_name = song_caller()
    score = (int(music_number)-1)

    for key, value in song_name.items():
        if key == "songs":
            songs = song_name["songs"]
            song_list = songs["song"]
            song_dict = song_list[score]
            return song_dict
    return 0


def artist_return(music_number):
    song_dict = song_return(music_number)

    for key, value in song_dict.items():
        if key == "artists":
            artists = song_dict[key]
            artist = artists["artist"]
            artist_dict = artist[0]
            return artist_dict
    return 0


def search_return(data, string_data):
    search_info = search_caller(data, string_data)

    if data == "artist_search":
        artist = search_info['artists']
        artist_list = artist['artist']
        pprint(artist_list)
        return artist_list

    elif data == "music_search":
        songs = search_info['songs']
        song_list = songs['song']
        pprint(song_list)
        return song_list

    else:
        albums = search_info['albums']
        album_list = albums['album']
        pprint(album_list)
        return album_list


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
