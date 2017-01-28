# -*- coding: utf-8 -*-

import sys
from bs4 import BeautifulSoup

data = ""
for line in sys.stdin:
    data += line
soup = BeautifulSoup(data, 'html.parser')

f = soup.find('div',id='rankingDetailAjaxContainer').find('table',class_='mega-table').find('tbody')
trs = f.findAll('tr')

for tr in trs:
    id = tr.find('td',class_='player-cell').find('a',{'href':True})['href'].rstrip().lstrip().replace('/en/players/','').replace('/overview','')
    player = tr.find('td',class_='player-cell').find('a').find(text=True).rstrip().lstrip()
    rank = tr.find('td',class_='rank-cell').find(text=True).rstrip().lstrip()
    points = tr.find('td',class_='points-cell').find('a').find(text=True).rstrip().lstrip().replace('.','').replace(',','')
    print  id+','+player+','+rank+','+points
