import urllib.request

import regex as re

with open(r'C:\Users\hp\Desktop\misc\SE Project\FantasicFour\Temp\log.txt', 'r') as file:
    data = file.read().replace('\n', '')
m = re.search('https://cf-hls-media.sndcdn.com/playlist/(.+?)"},', data)
if m:
    found = m.group(1)
url = ("https://cf-hls-media.sndcdn.com/playlist/" + found)

urllib.request.urlretrieve(url, r"C:\Users\hp\Desktop\misc\SE Project\FantasicFour\Temp\playlist.m3u")
