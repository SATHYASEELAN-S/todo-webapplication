from django.shortcuts import render,redirect
from django.contrib import messages
from base.form import TaskForm  ,TaskForm1
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User,auth
from base.models import Task

c=False
def loginpage(request):
    post='login'
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)

        if user is None:
            messages.error(request,"Password and Username Wrong")
            return redirect("login")
        else:
            login(request,user)
            global c
            c=True
            return redirect("home")
    context={'post':post}
    if c:
        return redirect("home")
    else:
        return render(request,'base/login.html',context)

def logoutpage(request):
    logout(request)
    global c
    c=False
    return redirect("/")

def register(request):
    post='register'
    context={'post':post}

    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        password1=request.POST["password1"]
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]

        if password1==password :
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists() :
                messages.error(request,"username or email already exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save()
                login(request,user)
                return redirect("home")
        else:
            messages.error(request,"password not matching....")
            return redirect('register')
    if c:
        return redirect("home")
    else:
         return render(request,'base/login.html',context)

def home(request):
    q=request.GET.get('q') if request.GET.get('q')!= None else " "
    if q!=" ":
        tasks=Task.objects.filter(taskfield__icontains=q)   
    else:
        tasks=Task.objects.all()
    for i in tasks:
        pid=i.id
    
    form=TaskForm()
    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            updatehost=Task.objects.get(id=(pid+1))
            updatehost.host=request.user
            updatehost.save()
            return redirect("home")
    context={"form":form,"tasks":tasks}
    if c:
        return render(request,'base/index.html',context)
    else:
        return redirect("login")
    
def updated(request,pk):
    getask=Task.objects.get(id=pk)
    form=TaskForm1(instance=getask)
    if request.method=="POST":
        form=TaskForm1(request.POST,instance=getask)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            messages.error(request,"check")
            return redirect("home")
    return render(request,'base/update.html',{"form":form})

def deleted(request,pk):
    form=Task.objects.get(id=pk)
    if request.method=="POST":
        form.delete()
        return redirect("home")
    return render(request,"base/deleted.html",{"form":form})