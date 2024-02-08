from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as logouts, authenticate, login

from .forms import StaffRegistrationForm, StaffLoginForm

def register_staff(request):
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')   
    else:
        form = StaffRegistrationForm()
    return render(request, 'register.html', {'form': form})


def staff_login(request):
    if request.method == 'POST':
        form = StaffLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to dashboard upon successful login
            else:
                form.add_error(None, 'Invalid email or password')
        
    else:
        form = StaffLoginForm()
        
    return render(request, 'login.html', {'form': form})







# def login(request) :
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
            
#             if user:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 form.add_error(None, 'Invalid username or password.')
#     else:
#         form = AuthenticationForm()

#     return render(request, 'login.html', {'form': form})


def dashboard(request) : 
    return render(request, 'dashboard.html')


def get_patients(request):
     return render(request, 'patients.html')



# def dashboard(request) : 
#     return render(request, 'dashboard.html')



def custom_404(request, exception):
    return render(request, '404.html', {'exception': exception}, status=404)