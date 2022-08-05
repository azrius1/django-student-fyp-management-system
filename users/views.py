from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.models import Group

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data.get('group')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            messages.success(request, f'The Account has been created! They are now able to login.')
            return redirect('blog-home')
    else:
        form = UserRegistrationForm()
    return render(request,'users/register.html',{'form': form})


    