from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Type
# Create your views here.


class IndexView(View):

    def get(self, request):
        templete_name = 'polls/index.html'
        allTypes = Type.objects.all()
        context = {
        'allTypes': allTypes
        }
        return render(request, 'polls/index.html', context)
