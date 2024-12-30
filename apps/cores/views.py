from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from apps.jobs.models import Job

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log the user in
            login(request, user)
            return redirect('frontpage')
    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})

def frontpage(request):
    jobs = Job.objects.all()[0:3]

    return render(request, 'cores/frontpage.html', {'jobs': jobs})