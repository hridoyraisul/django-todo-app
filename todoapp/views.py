from django.shortcuts import render, redirect
from .models import Todo

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

def about(request):
    return render(request, 'todoapp/about.html')
