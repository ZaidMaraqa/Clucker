from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, LogInForm, PostForm
from .models import Post, User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required


def login_prohbited(view_function):
    def modified_view_function(request):
        if request.user.is_authenticated:
            return redirect('feed')
        else:
            return view_function(request)
    return modified_view_function

@login_required
def feed(request):
    form = PostForm()
    return render(request, 'feed.html', {'form': form})

@login_prohbited
def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                redirect_url = request.POST.get('next') or 'feed'
                return redirect(redirect_url)
        messages.add_message(request, messages.ERROR, "The credenitals provided were invalid")
    form = LogInForm()
    next = request.GET.get('next') or ''
    return render(request, 'log_in.html', {'form': form, 'next' : next})

def home(request):
    return render(request, 'home.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('feed')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {"form": form})

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

@login_required
def show_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except ObjectDoesNotExist:
        return redirect('user_list')
    else:
        return render(request, 'show_user.html', {'user': user})

def new_post(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            current_user = request.user
            form = PostForm(request.POST)
            if form.is_valid():
                text = form.cleaned_data.get('text')
                post = Post.objects.create(author=current_user, text=text)
                return redirect('feed')
            else:
                return render(request, 'feed.html', {'form': form})
        else:
            return redirect('log_in')
    else:
        return HttpResponseForbidden()
