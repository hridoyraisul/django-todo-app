from django.shortcuts import render, redirect
from .models import *
from .utils.response import ResponseUtil
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from .forms import TodoForm, UserRegistrationForm, UserLoginForm

User = get_user_model() 

def tasks(request):
    try:
        todos = Todo.objects.all()
        todos_list = list(todos.values())
        return ResponseUtil.apiResponse('Fetched Successfully', todos_list, 200)
    except Exception as e:
        return ResponseUtil.apiResponse('An error occurred', str(e), 500)
    

def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            Todo.objects.create(text=form.cleaned_data['text'])
            return redirect('/todo')
    else:
        form = TodoForm()

    todos = Todo.objects.all()
    context = {'form': form, 'todos': todos}
    return render(request, 'todoapp/index.html',context)

def deleteTodo(request, id):
    Todo.objects.get(id=id).delete()
    return redirect('/todo')

@login_required
def about(request):
    return render(request, 'todoapp/about.html')

def userRegistration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            hashedPassword = make_password(password)
            user = User.objects.create(name=name, email=email, password=hashedPassword)
            login(request, user)
            return redirect('/todo')
    else:
        form = UserRegistrationForm()

    return render(request, 'todoapp/user_registration.html', {'form': form})


def userLogin(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(email=email)
                
                if not user.is_active:
                    return render(request, 'todoapp/user_login.html', {'form': form, 'error': 'Your account is deactivated'})

                if not check_password(password, user.password):
                    return render(request, 'todoapp/user_login.html', {'form': form, 'error': 'Invalid password'})

                user = authenticate(request, email=email, password=password)

                if user is not None:
                    login(request, user)
                    next_url = request.POST.get('next', '/todo')
                    return redirect(next_url)
                else:
                    return render(request, 'todoapp/user_login.html', {'form': form, 'error': 'Invalid email or password'})

            except User.DoesNotExist:
                return render(request, 'todoapp/user_login.html', {'form': form, 'error': 'Invalid email or password'})

    else:
        form = UserLoginForm()

    return render(request, 'todoapp/user_login.html', {'form': form})


# def userLogin(request):
#     if request.method == 'POST':
#         try:
#             email = request.POST.get('email').strip()
#             password = request.POST.get('password').strip()
#             user = User.objects.get(email=email)

#             if not user.is_active:
#                 return render(request, 'todoapp/user_login.html', {'error': 'Your account is deactivated'})

#             if not check_password(password, user.password):
#                 return render(request, 'todoapp/user_login.html', {'error': 'Invalid password'})

#             user = authenticate(request, email=email, password=password)

#             if user is not None:
#                 login(request, user)
#                 next_url = request.POST.get('next', '/todo')
#                 return redirect(next_url)
#             else:
#                 return render(request, 'todoapp/user_login.html', {'error': 'Invalid email or password'})

#         except User.DoesNotExist:
#             return render(request, 'todoapp/user_login.html', {'error': 'Invalid email or password'})
    
#     return render(request, 'todoapp/user_login.html')

def userLogout(request):
    logout(request)
    return redirect('/todo')
