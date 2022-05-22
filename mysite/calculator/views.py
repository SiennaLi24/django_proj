from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Type
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


class LogsView(View):

    def post(self, request, username):
        template_name = 'polls/logs.html'
        allTypes = Type.objects.all()
        context = {
        'allTypes': allTypes
        }
        return render(request, 'polls/logs.html', context)
        if 'logout' in request.POST.keys():
            logout(request)
        #return render(request, 'polls/login', redirect to login page)

class IndexView(View):
    def get(self, request):
        form = AuthenticationForm()
        context = {
            'form':form
        }
        return render (request, 'polls/login.html', context)
    def post(self, request):
        if 'logout' in request.POST.keys():
            logout(request)
            form = AuthenticationForm()

        else:
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username = username, password = password)
                if user is not None:
                    login(request, user = user)
        context = {
            'form': form
        }

        return render(request, 'polls/login.html', context)
