from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout


# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')


def logoutuser(request):
    logout(request)
    return redirect('/login')


def Signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password1']
        confirm_password = request.POST['password2']

        if password != confirm_password:
            return redirect('/register')

        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return render(request, 'login.html')
    return render(request, "signup.html")
    
def loginuser(request):
    if request.method=="POST":
        username= request.POST.get('username')
        password=request.POST.get('password')
     
        # check if user has entered correct credentials
        
        user = authenticate(username=username, password=password)
        if user is not None: 
            login(request, user)    
            return redirect("/")
        else:
            
            return render(request,'login.html')
    return render(request,'login.html')
   

def logoutuser(request):
    logout(request)
    return redirect('/login')
  