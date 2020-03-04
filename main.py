from bs4 import BeautifulSoup
from inotify_simple import INotify, flags

from db import *

def parseXml(rss):
    soup = BeautifulSoup(rss, 'lxml')
    html = soup.find_all('description')[1]
    tr = html.find_all('tr')

    for i in tr:
        if 'Time' in i.select('th')[0].text:
            dtime = i.select('td')[0].text
        elif 'Position' in i.select('th')[0].text:
            coords = i.select('td')[0].text
            latitude = coords.split(",")[0].split("°")[0]
            longitude = coords.split(",")[1].split("°")[0][1:]
        elif 'Major Place:' in i.select('th')[0].text:
            pass
        elif 'Place' in i.select('th')[0].text:
            position = i.select('td')[0].text
        elif 'Depth' in i.select('th')[0].text:
            depth = i.select('td')[0].text
        elif 'Magnitude' in i.select('th')[0].text:
            magnitude = i.select('td')[0].text

    return earthquakes(
            datetime = dtime,
            latitude=latitude,
            longitude=longitude,
            position=position,
            depth=depth,
            magnitude=magnitude)

path = './feed.rss'
wf = flags.MODIFY

while True:
    inotify = INotify()
    wd = inotify.add_watch(path, wf)
    for event in inotify.read():
        rss = open(path)
        print(parseXml(rss).datetime)
