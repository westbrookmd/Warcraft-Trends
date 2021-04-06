from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()
Bugs = 40
number = [725,724,722,721,720,719,718,717,716,715,714,713,712,711,709,708,705,702,701,700,699,698,697,696,694,689]
author = []
state = []
group_class = ["Death Knight","Rogue: Subtlety""Priest: Shadow","Rogue: Assassination",
"Rogue: Assassination","Warlock: Affliction","Rogue: Subtlety",
"Hunter","Priest","Rogue","Death Knight","Death Knight","Mage","Hunter","Paladin","Rogue","Mage",
"Death Knight","Priest","Rogue","Priest","Mage","Mage","Mage","Priest","Shaman"]
priests = sum('Priest' in s for s in group_class)
Hunters = sum('Hunter' in s for s in group_class)
Rogues = sum('Rogue' in s for s in group_class)
Warlock = sum('Warlock' in s for s in group_class)
Death_Knights = sum('Death Knight' in s for s in group_class)
Mages = sum('Mage' in s for s in group_class)
Shamans = sum('Shaman' in s for s in group_class)
bug_count = len(number)

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
        qs_count = User.objects.all().count()
        labels = ["Total Bugs", "Priests", "Hunters", "Rogues", "Warlocks", "Death Knights", "Mages", "Shamans"]
        default_items = [bug_count, priests, Hunters, Rogues, Warlock, Death_Knights, Mages, Shamans]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)

