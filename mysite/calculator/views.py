from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Type
from .forms import TypeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


class LogsView(View):
    template_name = 'polls/logs.html'
    def get(self, request, username):
        if 'logout' in request.POST.keys():
            logout(request)
            form = AuthenticationForm()
        allTypes = Type.objects.all()
        context = {
        'allTypes': allTypes
        }
        return render(request, 'polls/logs.html', context)

class CreateRate(View):
    template_name = 'polls/createFoodPost.html'
    def post(self, request, username):
        if request.method == 'POST':
            form = TypeForm(request.POST)

            if form.is_valid():
                foodPost = form.save(commit = False)
                foodPost.user = user
                foodPost.save()

                return render(request, 'polls/createFoodPost.html', {'form':form})

            else:
                form = TypeForm()
                return render(request, 'polls/createFoodPost.html', {'form':form})

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
