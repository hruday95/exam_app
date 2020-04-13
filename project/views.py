from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from project.forms import SignUpForm


# @login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # form = SignUpForm(request.POST, instance=request.user.signupform_profile)
        if form.is_valid():
            print("testing",form.save())
            user = form.save()
          # load the profile instance created by the signal
          #   user.Signupform.birth_date = form.cleaned_data.get('birth_date')
            user.save()
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=user.username, password=raw_password)
        login(request, user)
        return redirect('home')

    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})


def instructions(request):
    return render(request, 'instructions.html')


def start_exam(request):
    return render(request, 'startexam.html')
