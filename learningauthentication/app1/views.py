from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm
from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'app1/index.html')

@login_required
def account(request):
    return HttpResponse("Login successful!!!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def registration(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)#Not commited so that image file can be processed as required
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['proflie_pic']

            profile.save()

            registered = True
            user_form = UserForm()
            profile_form = UserProfileInfoForm()
            return render(request, 'app1/registration.html', {'registered' : registered,
                                                                'user_form' : user_form,
                                                                    'profile_form' : profile_form})

        else:
            print(user_form.errors, profile_form.errors)

    else:   #if method is GET which will be first time the page is accessed
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'app1/registration.html',
                            {'registered' : registered,
                             'user_form' : user_form,
                              'profile_form' : profile_form}
                              )

def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active!!")
        else:
            return HttpResponse("Invalid login request")
    else:
        return render(request, 'app1/login.html')
