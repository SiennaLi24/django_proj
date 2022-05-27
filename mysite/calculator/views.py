from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import Type, UserProfile, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from pprint import pprint
from .forms import UpdateProfileForm, CommentForm, RegistrationForm, CreatePostForm
from django import forms
import datetime
from django.utils import timezone
from django.contrib import messages
from PIL import Image
# Create your views here.
#ask about instance
class RegisterView(View):
    def get(self, request):
        allTypes = Type.objects.all()
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            context = {
                'allTypes':allTypes
            }
            return render(request, "polls/logs.html", context)
        messages.error(request, "Unsuccessful registration. Invalid information.")
        print("1")
        form = RegistrationForm()
        context = {
            'form':form,
        }
        return render(request, "polls/register.html", context)

    def post(self, request):
        allTypes = Type.objects.all()
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            context = {
                'allTypes':allTypes
            }
            return render(request, "polls/logs.html", context)
        messages.error(request, "Unsuccessful registration. Invalid information.")
        form = RegistrationForm()
        context = {
            'form':form,
        }
        return render(request, "polls/register.html", context)
class DeletePost(View):
    def get(self, request, type_id, username):
        return render(request, 'polls/unauthorized.html')

    def post(self, request, type_id, username):
        type = get_object_or_404(Type, pk = type_id)
        user = User.objects.get(username = username)
        userProfile = UserProfile.objects.get(user = user)
        exist = True
        object = Type.objects.get(pk = type_id)
        object.delete()
        userTypes = Type.objects.filter(foodPost = user)
        print(userTypes)
        context = {
            'userProfile':userProfile,
            'exist':exist,
            'userTypes':userTypes,
        }
        return render(request, 'polls/profile.html', context)

class UserView(View):
    def get(self, request, type_id, foodPost):
        return render(request, 'polls/unauthorized.html')
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
    def get(self, request, type_id, username):
        return render(request, 'polls/unauthorized.html')
    def post(self, request, username, type_id):
        type = get_object_or_404(Type, pk = type_id)
        user = User.objects.get(username = username)
        form = CreatePostForm(request.POST, request.FILES)
        context = {
            'type':type,
            'form':form,
        }
        return render(request, 'polls/editPost.html', context)

class EditPost(View):
    def get(self, request, type_id, username):
        return render(request, 'polls/unauthorized.html')
    def post(self, request, username, type_id):
        type = get_object_or_404(Type, pk = type_id)
        exist = True
        user = User.objects.get(username = username)
        userProfile = UserProfile.objects.get(user = user)
        if request.method == 'POST':
            form = CreatePostForm(request.POST, request.FILES, instance = type)
            if form.is_valid():
                form.save()
                foodName = form.cleaned_data['foodName']
                foodType = form.cleaned_data['foodType']
                foodRate = form.cleaned_data['foodRate']
                foodComment = form.cleaned_data['foodComment']
                foodImage = request.FILES['foodImage']
                type.foodName = foodName
                type.foodType = foodType
                type.foodRate = foodRate
                type.foodImage = foodImage
                type.save()
            allTypes = Type.objects.all()
            context = {
                'form':form,
                'userProfile':userProfile,
                'allTypes':allTypes,
                'exist':exist,
                'type':type,
            }
            return render(request, 'polls/logs.html', context)
        else:
            form = CreatePostForm()

        context = {
            'form':form,
            'userProfile':userProfile,
            'allTypes':allTypes,
            'exist':exist,
            'type':type,
        }
        return render(request, 'polls/editProfile.html', context)



class DetailView(View):
    print("1a")
    def get(self, request, type_id):
        return render(request, 'polls/unauthorized.html')
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
    def get(self, request, username):
        return render(request, 'polls/unauthorized.html')
    def post(self, request, username):
        allTypes = Type.objects.all()
        user = User.objects.get(username = username)
        userProfile = UserProfile.objects.get(user = user)
        print(userProfile.location)
        if request.method == 'POST':
            form = UpdateProfileForm(request.POST, request.FILES, instance = userProfile)
            print(userProfile)
            if form.is_valid():
                print("yes")
                form.save()
                location = form.cleaned_data['location']
                qualifications = form.cleaned_data['qualifications']
                image = request.FILES['image']
                userProfile.location = location
                userProfile.qualifications = qualifications
                userProfile.image = image
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
    def get(self, request, username):
        return render(request, 'polls/unauthorized.html')
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
            form = UpdateProfileForm(request.POST, request.FILES)
            context = {
                'exist':exist,
                'form':form,
                'userTypes':userTypes,
            }
            if form.is_valid():
                form.save()
                print("3")
                exist = True
                location = form.cleaned_data['location']
                qualifications = form.cleaned_data['qualifications']
                image = request.FILES['image']
                userProfile = UserProfile(location = location, qualifications = qualifications, image = image)
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
        return render(request, 'polls/unauthorized.html')


class CreateRate(View):
    def get(self, request, username):
        return render(request, 'polls/unauthorized.html')
    def post(self, request, username):
        form = CreatePostForm()
        allTypes = Type.objects.all()
        context = {
            'form':form,
            'allTypes':allTypes,
        }
        print(allTypes)
        return render(request, 'polls/createFoodPost.html', context)


class SaveRate(View):
    def get(self, request, username):
        return render(request, 'polls/unauthorized.html')
    def post(self, request, username):
        allTypes = Type.objects.all()
        if request.method == 'POST':
            form = CreatePostForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                foodName = form.cleaned_data['foodName']
                foodType = form.cleaned_data['foodType']
                foodRate = form.cleaned_data['foodRate']
                foodComment = form.cleaned_data['foodComment']
                foodImage = request.FILES['foodImage']
                newPost = Type(foodName = foodName, foodType = foodType, foodRate = foodRate, foodComment = foodComment, foodImage = foodImage)
                newPost.foodPost = request.user
                newPost.save()
                allTypes = Type.objects.all()
                context = {
                    'allTypes':allTypes,
                    'form':form,
                }
                return render(request, 'polls/logs.html', context)
        else:
            form = CreatePostForm()

        context = {
            'form':form,
            'allTypes':allTypes,
        }
        return render(request, 'polls/editProfile.html', context)



class IndexView(View):
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
