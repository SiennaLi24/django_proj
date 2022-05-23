from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Type
from .forms import TypeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from pprint import pprint
# Create your views here.


class LogsView(View):
    template_name = 'polls/logs.html'
    def post(self, request, username):
        if 'logout' in request.POST.keys():
            logout(request)
            form = AuthenticationForm()
        allTypes = Type.objects.all()
        context = {
        'allTypes': allTypes
        }
        return render(request, 'polls/logs.html', context)
    def get(self, request, username):
        if request.user.is_authenticated:
            if 'logout' in request.POST.keys():
                logout(request)
                form = AuthenticationForm()
            allTypes = Type.objects.all()
            context = {
            'allTypes': allTypes
            }
            return render(request, 'polls/logs.html', context)
        else:
            pass




class CreateRate(View):
    template_name = 'polls/createFoodPost.html'
    def post(self, request, username):
        allTypes = Type.objects.all()
        context = {
            'allTypes':allTypes,
        }
        print(allTypes)
        return render(request, 'polls/createFoodPost.html', context)




class SaveRate(View):
    def post(self, request, username):
        pprint(request.POST)
        foodName = request.POST['foodName']
        foodType = request.POST['foodType']
        foodRate = request.POST['foodRate']
        newPost = Type(foodName = foodName, foodType = foodType, foodRate = foodRate)

        newPost.foodPost = request.user
        newPost.save()
        allTypes = Type.objects.all()
        context = {
            'allTypes':allTypes,
        }

        print("yes")
        return render(request, 'polls/logs.html', context)




class IndexView(View):
    template_name = 'polls/logs.html'
    def get(self, request):
        form = AuthenticationForm()
        allTypes = Type.objects.all()
        context = {
            'form':form,
            'allTypes': allTypes
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
