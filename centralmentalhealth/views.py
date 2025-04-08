from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# 🌀 LOADING PAGE
def loading_view(request):
    return render(request, 'loading.html')


# 🏠 HOME PAGE (Login Required)
@login_required(login_url='signin')
def home_view(request):
    return render(request, 'home.html')


# 📊 TRACKER PAGE (Login Required)
@login_required(login_url='signin')
def tracker_view(request):
    return render(request, 'tracker.html')

@login_required(login_url='signin')
def logger_view(request):
    return render(request, 'Logger.html')


# 📝 SIGNUP
def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists!")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email is already in use!")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Account created successfully!")
                return redirect("signin")
        else:
            messages.error(request, "Passwords do not match!")

    return render(request, "signup.html")


# 🔐 SIGNIN
def signin_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")  # Redirect to home after login
        else:
            messages.error(request, "Invalid credentials!")

    return render(request, "signin.html")


# 🚪 LOGOUT
def logout_view(request):
    logout(request)
    return redirect("signin")
