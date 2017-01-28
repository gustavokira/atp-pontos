# -*- coding: utf-8 -*-

import os
import json

weeks = {}


fileNames = os.listdir("csv")
for fileName in fileNames:
    file = open("csv/"+fileName, 'r')
    week = {}
    for line in file:
        columns = line.rstrip().lstrip().split(",")
        id = columns[0].split("/")[1]
        week[id] = int(columns[3])
        weeks[fileName.split("csv")[0].replace(".","")] = week

print json.dumps(weeks,indent=1)
