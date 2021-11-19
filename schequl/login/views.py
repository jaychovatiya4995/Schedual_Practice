from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserInfo
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def index(request):
    return render(request, 'login.html')


def regform(request):
    return render(request, 'registration.html')


def login(request):
    if request.method == 'POST':
        try:
            Userdetails = UserInfo.objects.get(email=request.POST['email'], password=request.POST['psw'])
            print(Userdetails)
            request.session['email']=Userdetails.email
            return render(request, 'home.html')
        except ObjectDoesNotExist as e:
            messages.error(request, 'Username / password is unvalid ..!!')

    return redirect('index')


def registration(request):
    if request.method == 'POST':
        fnm = request.POST['fnm']
        lnm = request.POST['lnm']
        birth = request.POST['bd']
        gen = request.POST['sex']
        marital = request.POST['marital']
        mobile = request.POST['mo']
        email = request.POST['email']
        address = request.POST['add']
        password = request.POST['psw']
        password1 = request.POST['psw1']
        if password1 != password:
            messages.error(request, 'password must be same')
        else:
            try:
                UserInfo(fnm=fnm, lnm=lnm, birth=birth, gen=gen, marital=marital, mobile=mobile, email=email, address=address, password=password).save()
                messages.success(request, 'Register Successfully')
                return render(request, 'home.html')
            except:
                messages.error(request,'Something want to wrong !!')
                return redirect('regform')

    return redirect('regform')


def logout(request):
    return redirect('index')


def forgot(request):
    return redirect('index')