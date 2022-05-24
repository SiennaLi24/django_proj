from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Type, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from pprint import pprint
from .forms import UpdateProfileForm
from django import forms
#from .forms import UpdateProfileForm
# Create your views here.


class EditView(View):
    template_name = 'polls/editProfile.html'
    def post(self, request, username):
        allTypes = Type.objects.all()
        user = User.objects.get(username = username)
        userProfile = UserProfile.objects.get(user = user)
        print(userProfile.location)
        if request.method == 'POST':
            form = UpdateProfileForm(request.POST)
            print("here")
            if form.is_valid():
                print("yes")
                location = form.cleaned_data['location']
                qualifications = form.cleaned_data['qualifications']
                userProfile.location = location
                userProfile.qualifications = qualifications
                userProfile.save()
                context = {
                    'form':form,
                    'userProfile':userProfile,
                    'allTypes':allTypes,
                }
                return render(request, 'polls/logs.html', context)
        else:
            form = UpdateProfileForm()
        #edittedProfile = UserProfile(user = user, location = location, qualifications = qualifications)
        #userProfile.location = request.POST['location']
        #userProfile.qualifications = request.POST['qualifications']
    #    userProfile.save()
        context = {
            'form':form,
            'userProfile':userProfile,
            'allTypes':allTypes,
        }
        return render(request, 'polls/editProfile.html', context)


class ProfileView(View):
    def post(self, request, username):
        user = User.objects.get(username = username)
        exist = True
        try:
            userProfile = UserProfile.objects.get(user = user)
        except:
            exist = False
            form = UpdateProfileForm(request.POST)
            if form.is_valid():
                location = form.cleaned_data['location']
                qualifications = form.cleaned_data['qualifications']
                userProfile = UserProfile(location = location, qualifications = qualifications)
                userProfile.user = request.user
                userProfile.save()
            context = {
                'exist':exist,
                'form':form,
            }
            return render(request, 'polls/profile.html', context)
        print(exist)
        context = {
            'exist':exist,
            'userProfile':userProfile,
        }
        return render(request, 'polls/profile.html', context)
    #def post(self, request, username):
    #    user = User.objects.get(username = username)
    #    exist = True
    #    try:
    #        userProfile = UserProfile.objects.get(user = user)
    #    except:
    #        exist = False
    #        if "location" in request.POST.keys():
    #            pprint(request.POST)
    #            location = request.POST['location']
    #            qualifications = request.POST['qualifications']
    #            newProfile = UserProfile(user = user, location = location, qualifications = qualifications)
    #            newProfile.user = request.user
    #            newProfile.save()
    #        return render(request, 'polls/profile.html', { 'exist':exist })
    #    print(exist)
    #    context = {
    #        'exist':exist,
    #        'userProfile':userProfile,
    #    }
    #    return render(request, 'polls/profile.html', context)
    #def get (if user is not none/if user is not the logged in user)

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
