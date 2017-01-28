# -*- coding: utf-8 -*-

import os
import json

players = {}

fileNames = os.listdir("csv")
for fileName in fileNames:
    file = open("csv/"+fileName, 'r')
    for line in file:
        columns = line.rstrip().lstrip().split(",")

        if columns[0] not in players:
            player = {}
            player["nome"] = columns[1]
            player["weeks"] = []
            players[columns[0]] = player

        week = {}
        week["pt"] = int(columns[3])
        week["w"] = fileName.replace(".csv","")
        players[columns[0]]["weeks"].append(week)

print json.dumps(players,indent=1)
