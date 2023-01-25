from django.shortcuts import render,redirect
from . models import Customer
from . forms import Customerform
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.

def loginPage(request):
    authenticationForm=AuthenticationForm()
    if request.method == 'POST':
        authenticationForm=AuthenticationForm(request, data=request.POST or None)
        if authenticationForm.is_valid():
            username=authenticationForm.cleaned_data['username']
            password=authenticationForm.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user=user)
                return redirect('home')        
    context={'authenticationForm':authenticationForm}
    return render(request,'login.html',context)

@login_required(login_url="login")
def home(request):
    context={}
    return render(request,'home.html',context)

@login_required(login_url="login")
def logoutuser(request):
    if not request.user.is_authenticated:
        return redirect("login")
    logout(request)
    return redirect("login")

def registration(request):
    usercreationform=UserCreationForm()
    if request.method == 'POST':
        usercreationform=UserCreationForm(request.POST or None)
        if usercreationform.is_valid():
            username=usercreationform.cleaned_data['username']
            password=usercreationform.cleaned_data['password1']
            usercreationform=usercreationform.save()
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user=user)
                return redirect('home')        

    context={'usercreationform':usercreationform}
    return render(request,'registration.html',context)


def view_cus(request):
    form = Customerform()
    customers = Customer.objects.all()
    context = {"customers": customers ,"form": form}
    return render(request, "view_customers.html", context)


def add_custom(request):
    form = Customerform()
    if request.method == "POST":
        form = Customerform(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, "customer was added succesfully")
            return redirect("home")
        else:
            messages.error(request, "error occured")
    context={"form": form}
    return render(request,'add_customers.html',context)