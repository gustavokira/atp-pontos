# -*- coding: utf-8 -*-

import sys
from bs4 import BeautifulSoup

data = ""
for line in sys.stdin:
    data += line
soup = BeautifulSoup(data, 'html.parser')

f = soup.find('div',id='filterHolder')
uls = f.findAll('ul',class_='dropdown')
lis = uls[0].findAll('li')

for l in lis:
	print(l.find(text=True).replace('.','-').strip().encode('utf-8'))
