from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout
# Create your views here.
def register(request):
    if request.method=="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'welcome {username}, your account has been successfully created')
            return redirect('myapp:index')
    form = RegisterForm()
    return render(request,'users/register.html',{'form':form})

def logout_view(request):
    logout(request)
    return render(request,'users/logout.html')

@login_required
def profile(request):
    return render(request,'users/profile.html')

