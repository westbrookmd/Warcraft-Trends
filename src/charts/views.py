from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
import openpyxl, json
#import json, requests
#import pandas as pd

#sheetName = '1JCVnNPNvjvecRMULcCNffGjbYFKb7Are0DvQcaS7G_A'
#ss = ezsheets.Spreadsheet(sheetName)

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb['Sheet']

maxColumn = sheet.max_column
print("Sheet Maximum Column: " + str(maxColumn))

maxRow = sheet.max_row
print("Sheet Maximum Row: " + str(maxRow))

produceNames = []
for i in range(2, 50):
    cellData = sheet.cell(row = i, column = 1)
    produceNames.append(cellData.value)
print(produceNames)

produceValues = []
for i in range(2, 50):
    cellData = sheet.cell(row = i, column = 2)
    produceValues.append(cellData.value)
print(produceValues)


with open('wow_issues.json') as json_file:
    wowData = json.load(json_file)

wowClasses = []
wowClassesUnclassified = 0
for issue in range(len(wowData)-1):
    try:
        print ("Issue " + str(issue) + " Title: " + str(wowData[issue]['title']))
        print ("Class: " + str(wowData[issue]['labels'][-1]['name']))
        wowClasses.append(wowData[issue]['labels'][-1]['name'])
    except:
        wowClassesUnclassified += 1



user = get_user_model()
bugs = 40
number = [725,724,722,721,720,719,718,717,716,715,714,713,712,711,709,708,705,702,701,700,699,698,697,696,694]
author = []
state = []
group_class = ["Death Knight","Rogue: Subtlety""Priest: Shadow","Rogue: Assassination",
"Rogue: Assassination","Warlock: Affliction","Rogue: Subtlety",
"Hunter","Priest","Rogue","Death Knight","Death Knight","Mage","Hunter","Paladin","Rogue","Mage",
"Death Knight","Priest","Rogue","Priest","Mage","Mage","Mage","Priest","Shaman"]
Priests = sum('Priest' in s for s in wowClasses)
Hunters = sum('Hunter' in s for s in wowClasses)
Rogues = sum('Rogue' in s for s in wowClasses)
Warlocks = sum('Warlock' in s for s in wowClasses)
DeathKnights = sum('Death Knight' in s for s in wowClasses)
Mages = sum('Mage' in s for s in wowClasses)
Shamans = sum('Shaman' in s for s in wowClasses)
DemonHunters = sum('Demon Hunter' in s for s in wowClasses)
Druids = sum('Druid' in s for s in wowClasses)
Monks = sum('Monk' in s for s in wowClasses)
Paladins = sum('Paladin' in s for s in wowClasses)
Warriors = sum('Warrior' in s for s in wowClasses)

#bug_count = (priests + Hunters + Rogues +  Warlocks +  Death_Knights +  Mages + Shamans)/10
#produce_count = len(produceNames)

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {"customers": 10})



def get_data(request, *args, **kwargs):
    data = {
        "Bugs": 1000,
        "Users": 10,
    }
    return JsonResponse(data) # http response


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = user.objects.all().count()
        labels = ["Priests", "Hunters", "Rogues", "Warlocks", "Death Knights", "Mages", "Shamans", "Demon Hunters", "Druids", "Monks", "Paladins", "Warriors"]
        #labels = produceNames
        default_items = [Priests, Hunters, Rogues, Warlocks, DeathKnights, Mages, Shamans, DemonHunters, Druids, Monks, Paladins, Warriors]
        
        #default_items = produceValues
        data = {
                "labels": labels,
                "default": default_items
        }
        return Response(data)

