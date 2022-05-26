from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import Type, UserProfile, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from pprint import pprint
from .forms import UpdateProfileForm, CommentForm
from django import forms
import datetime
from django.utils import timezone
# Create your views here.

class UserView(View):
    template_name = 'polls/userView.html'
    def post(self, request, foodPost, type_id):
        user = User.objects.get(username = foodPost)
        type = get_object_or_404(Type, pk = type_id)
        otherTypes = Type.objects.filter(foodPost = user)
        otherProfile = UserProfile.objects.get(user = user)
        context = {
            'otherTypes':otherTypes,
            'foodPost':foodPost,
            'otherProfile':otherProfile,
            'type':type,
        }
        return render(request, 'polls/userView.html', context)

class ViewPost(View):
    template_name = 'polls/editPost.html'
    def post(self, request, username, type_id):
        type = get_object_or_404(Type, pk = type_id)
        context = {
            'type':type,
        }
        return render(request, 'polls/editPost.html', context)

class EditPost(View):

    def post(self, request, username, type_id):
        type = get_object_or_404(Type, pk = type_id)
        exist = True
        user = User.objects.get(username = username)
        userProfile = UserProfile.objects.get(user = user)
        userTypes = Type.objects.filter(foodPost = user)
        type.foodName = request.POST['foodName']
        type.foodType = request.POST['foodType']
        type.foodRate = request.POST['foodRate']
        type.foodComment = request.POST['foodComment']
        type.save()
        context = {
            'type':type,
            'userProfile':userProfile,
            'userTypes':userTypes,
            'exist':exist,
        }

        return render(request, "polls/profile.html", context)
class DetailView(View):
    print("1a")
    template_name = 'polls/detailView.html'
    def post(self, request, type_id):
        print("2a")
        postComments = Comment.objects.filter(post = type_id)
        type = get_object_or_404(Type, pk = type_id)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            print("3a")
            context = {
                'form':form,
                'postComments':postComments,
                'type':type,
            }
            if form.is_valid():
                print("4a")
                ratePost = form.cleaned_data['ratePost']
                comment = form.cleaned_data['comment']
                newComment = Comment(ratePost = ratePost, comment = comment, pub_date=timezone.now())
                newComment.post = type
                print(type)
                newComment.save()
                print(comment)
                newPostComments = Comment.objects.filter(post = type_id)
                print(newPostComments)
                context['postComments'] = newPostComments

            return render(request, 'polls/detailView.html', context)
        else:
            form = CommentForm()
        context = {
            'form':form,
            'type':type,
            'postComments':postComments,
        }
        return render(request, 'polls/detailView.html', context)

class EditView(View):
    template_name = 'polls/editProfile.html'
    def post(self, request, username):
        allTypes = Type.objects.all()
        user = User.objects.get(username = username)
        userProfile = UserProfile.objects.get(user = user)
        print(userProfile.location)
        if request.method == 'POST':
            form = UpdateProfileForm(request.POST)
            print(userProfile)
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
        userTypes = Type.objects.filter(foodPost = user)
        try:
            userProfile = UserProfile.objects.get(user=user)
            print("1")
        except UserProfile.DoesNotExist:
            print("2")
            exist = False
            form = UpdateProfileForm(request.POST)
            context = {
                'exist':exist,
                'form':form,
                'userTypes':userTypes,
            }
            if form.is_valid():
                print("3")
                exist = True
                location = form.cleaned_data['location']
                qualifications = form.cleaned_data['qualifications']
                userProfile = UserProfile(location = location, qualifications = qualifications)
                userProfile.user = request.user
                userProfile.save()
                context["userProfile"] = userProfile
                context["exist"] = True

            return render(request, 'polls/profile.html', context)
        print("4")
        context = {
            'exist':exist,
            'userTypes':userTypes,
            'userProfile':userProfile,
        }
        return render(request, 'polls/profile.html', context)


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
        foodComment = request.POST['foodComment']
        newPost = Type(foodName = foodName, foodType = foodType, foodRate = foodRate, foodComment = foodComment)
        newPost.foodPost = request.user
        newPost.save()
        allTypes = Type.objects.all()
        context = {
            'allTypes':allTypes,
        }

        print(newPost.foodPost)
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
