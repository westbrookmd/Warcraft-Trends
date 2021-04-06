from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()
Bugs = 40



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
        labels = ["Bugs", "Total Users", "Yellow", "Green", "Purple", "Orange"]
        default_items = [Bugs, qs_count, 2, 3, 12, 2]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)

