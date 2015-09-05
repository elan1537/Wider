import urllib.request
import json
import random
import string
from pprint import pprint
import requests
import webbrowser

SECRET_KEY = 'miswneh8'
Client_id = "Your Client id"


def generate_state():
    c = string.ascii_letters + string.digits
    return ''.join(random.sample(c, 16))

def get_login():
    state = generate_state()
    url = "https://nid.naver.com/oauth2.0/authorize?client_id=" + Client_id \
          + "&response_type=code&redirect_uri=" + "http%3A%2F%2Fwider.0pe.kr" + "&state=" + state
    s = requests.session()
    r = s.get(url)
    webbrowser.open(r)


def get_block():
    url = "https://openapi.naver.com/blog/writePost.json"
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')

    data = json.loads(result)
    pprint(data)

    return data