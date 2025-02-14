from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password= password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are in')
            return redirect('dashboard')
        else:
            messages.error(request, 'invalid credentilas')
            return redirect('signup')
    else:
        return render(request, 'accounts/login.html')


def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password'] 

        if password == confirm_password:
            if User.objects.filter(username = username).exists():   
                messages.error(request, f'Username exists:{username}')             
                return redirect('signup')                
            elif User.objects.filter(email = email).exists():
                messages.error(request, f'Email already exists:{email}')
                return redirect('signup')
            else:
                user = User.objects.create_user(first_name = firstname,
                                            last_name = lastname,
                                            username = username,
                                            email = email,
                                            password= password)
                user.save()
                messages.success(request, 'Account created successfully')
                return redirect('login')
        else:
            messages.error(request, "Passwords doesn't match")
            return redirect('signup')
    else:
        return render(request, 'accounts/signup.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url="login")
def dashboard(request):
    return render(request, 'accounts/dashboard.html')