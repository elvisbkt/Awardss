from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .forms import UpdateProfileForm, UpdateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import CustomUser
from landing_page.models import Website
from .forms import CustomUserCreationForm

def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def profile(request, username, id):
    profile = CustomUser.objects.filter(username = username).first()
    websites = Website.objects.filter(posted_by = profile.pk)
    print(websites)
    print(profile.username)
    context = {
        "profile":profile,
        "websites":websites,
    }
    return render(request, 'profile.html', context)

@login_required
def update_profile(request, username, id):
    profile = CustomUser.objects.filter(username = username).first()
    print(profile.username)
    if request.method == 'POST':
        u_form = UpdateUserForm(request.POST, instance=request.user)
        p_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has successfully been updated!")
            return redirect ('profile', username, id)
    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = UpdateProfileForm(instance=request.user.profile)
        context = {
        "u_form":u_form,
        "p_form":p_form,
        "profile":profile,
    }
    return render(request, 'update_profile.html', context)

