from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm, ChangeForm
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views import generic
from random import random




class index(generic.ListView):
    template_name = "bizzfuzz/list.html"
    context_object_name = "users_list"
    
    def get_queryset(self):
        userModel = get_user_model()
        return userModel.objects.all() 


def details(request, user_id):
    userModel = get_user_model()
    userInstance = get_object_or_404(userModel, pk=user_id)
    context = {'user': userInstance}
    return render(request, 'bizzfuzz/details.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.birth_date = form.cleaned_data.get('birth_date')
            random_val = int(100*random())
            user.random_number = random_val
            user.save()
            return redirect('/')
    else:
        form = RegistrationForm()
 
    return render(request, 'bizzfuzz/reg_form.html', {'form': form})


def edit(request, user_id):
    userModel = get_user_model()
    userInstance = get_object_or_404(userModel, pk=user_id)
    if request.method == 'POST':
        form = ChangeForm(request.POST, instance=userInstance)
        # form = ChangeForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('/')
    else:
        form = ChangeForm()
 
    return render(request, 'bizzfuzz/edit.html', {'form': form, 'userInstance' : userInstance})


def delete(request, user_id):
    userModel = get_user_model()
    userInstance = get_object_or_404(userModel, pk=user_id)
    userInstance.delete() 

    return redirect("/")