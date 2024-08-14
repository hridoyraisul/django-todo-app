from django.shortcuts import render, redirect
from .models import *
from .utils.response import ResponseUtil
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required

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
        text = request.POST.get('text').strip()
        print(text)
        if text:
            Todo.objects.create(text=text)
        return redirect('/todo')
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'todoapp/index.html',context)

def deleteTodo(request, id):
    Todo.objects.get(id=id).delete()
    return redirect('/todo')

# @login_required
def about(request):
    return render(request, 'todoapp/about.html')

def userRegistration(request):
    if request.method == 'POST':
        name = request.POST.get('name').strip()
        email = request.POST.get('email').strip()
        password = request.POST.get('password').strip()
        confirm_password = request.POST.get('confirm_password').strip()

        if not all([name, email, password, confirm_password]):
            return render(request, 'todoapp/user_registration.html', {'error': 'Please fill all fields'})

        if password != confirm_password:
            return render(request, 'todoapp/user_registration.html', {'error': 'Passwords do not match'})

        if User.objects.filter(email=email).exists():
            return render(request, 'todoapp/user_registration.html', {'error': 'Email is already taken'})

        hashedPassword = make_password(password)
        User.objects.create(name=name, email=email, password=hashedPassword)
        return redirect('/todo')
    
    return render(request, 'todoapp/user_registration.html')



def userLogin(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email').strip()
            password = request.POST.get('password').strip()
            user = User.objects.get(email=email)

            if not user.is_active:
                return render(request, 'todoapp/user_login.html', {'error': 'Your account is deactivated'})

            if not check_password(password, user.password):
                return render(request, 'todoapp/user_login.html', {'error': 'Invalid password'})

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('/todo')
            else:
                return render(request, 'todoapp/user_login.html', {'error': 'Invalid email or password'})

        except User.DoesNotExist:
            return render(request, 'todoapp/user_login.html', {'error': 'Invalid email or password'})
    
    return render(request, 'todoapp/user_login.html')

def userLogout(request):
    logout(request)
    return redirect('/todo')
