from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Type
# Create your views here.
def calculate(request):
    return HttpResponse("answer")

class IndexView(View):
    templete_name = 'polls/index.html'
    def get(self, request):
        return HttpResponse("index")

def foodType(request):
    return HttpResponse ("<h1> answer </h1> <p> The recommended amount of carbs per day should be around 2000. You are currently around answer+amount </p>")
