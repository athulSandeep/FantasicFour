import requests

links = []
sess = requests.Session()
with open(r"C:\Users\hp\Desktop\misc\SE Project\Temp\playlist.m3u") as file:
    for line in file:
        if (line.startswith("http")):
            links.append(line.strip("\n"))
print(links)
with open(r"C:\Users\hp\Desktop\misc\SE Project\Downloads\Audio.mp3", 'wb') as f:
    for segment_uri in links:
        r = sess.get(segment_uri)
        f.write(r.content)
