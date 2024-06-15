
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required

# Create your views here.


    

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = NewUserForm()
    return render(request, 'users/register.html', {'form': form})
@login_required
def profilepage(request):
    return render(request, 'users/profile.html')
