from bs4 import BeautifulSoup

def convert(input_bytes):
    soup = BeautifulSoup(input_bytes, 'lxml')
    html = soup.find_all('description')[1]
    html = html.find_all('td')

    dtime = html[0]
    coords = td[1]
    position = td[2]
    depth = td[3]
    magnitude = td[4]
