from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignUpForm

# Create your views here.
def index(request):
    return render(request, "chat/index.html")

def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('chat:index')
    
    return render(request, "chat/signup.html", context={
        "form": form
    })