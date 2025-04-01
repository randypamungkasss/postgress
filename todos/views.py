from django.shortcuts import render, redirect
from .models import Todo
from django.views import View

# Create your views here.
class IndexView(View):
    def get(self, request):
        todos = Todo.objects.all()
        return render(request, 'index.html', {"todos": todos})
    
    def post(self,request):
        title = request.POST.get('title')
        task = request.POST.get('task')
        print(f'title: {title}, task: {task}')
        return redirect('index')

def index_view(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {"todos": todos})

def detail_view(request, id):
    todo = Todo.objects.get(id=id)
    return render(request, 'detail_view.html', {"todo":todo})