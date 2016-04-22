from django.shortcuts import render, redirect
from .forms import User
from .models import log_in

def home(request):
    return render(request, 'login/home.html', {})

def next(request):
	return render(request, 'login/next.html', {})

def new_user(request):
	if request.method == "POST":
		form = User(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			username =	post.username
			password = post.password
			post.save()
			p = log_in.objects.all()
			return render(request, 'login/user.html', {'p': p})
	else:
		form = User()
	return render(request, 'login/home.html')
    
"""
    form = User()
    return render(request, 'blog/post_edit.html', {'form': form})
"""