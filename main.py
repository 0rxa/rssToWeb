from flask import Flask, escape, request
from bs4 import BeautifulSoup
from eq import *
import os

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

    ret = Earthquake(
            datetime = dtime,
            latitude=latitude,
            longitude=longitude,
            position=position,
            depth=depth,
            magnitude=magnitude)
    return ret

app = Flask(__name__)

@app.route('/', methods=['POST'])
# @notification.post_notify()
def push():
    rss = request.files['data']
    rss.save('./tmpfile')
    if not rss:
        print("No file provided")
        return {}
    eq = parseXml(open('./tmpfile'))

    if not Earthquake.select()\
            .where(Earthquake.datetime == eq.datetime,\
                Earthquake.depth == eq.depth, \
                Earthquake.position == eq.position):
        eq.save()
    os.remove('./tmpfile')
    return {},200
    
app.run(debug=True, port=8008)
