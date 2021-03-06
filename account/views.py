from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegistrationForm, UploadPicture
from .models import User


"""def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                phone_number=cd['phone_number'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disable account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})
    """


def registration_user(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.save()
            return render(request, 'registration/registration_done.html', {'new_user': new_user})
    else:
        user_form = RegistrationForm()
    return render(request, 'registration/registration.html', {'user_form': user_form})


@login_required
def teleapp(request):
    return render(request, 'account/teleapp.html', {'teleapp': teleapp})


def upload(request):
    if request.method == 'POST':
        upload_photo = UploadPicture(request.POST, request.FILES)
        if upload_photo.is_valid():
            photo = upload_photo.save(commit=False)
            photo.save()
            return render(request, 'account/upload_done.html', {'photo': photo})
        else:
            HttpResponse("Not valid")
    else:
        upload_photo = UploadPicture()
    return render(request, 'account/test.html', {'upload_photo': upload_photo})

# Create your views here.
