from django.shortcuts import render, redirect
from .models import Todo
from django.views import View
from django.contrib import messages

# Create your views here.
class IndexView(View):
    def get(self, request):
        todos = Todo.objects.all()
        return render(request, 'index.html', {"todos": todos})
    
    def post(self,request):
        title = request.POST.get('title')
        task = request.POST.get('task')

        if not title and not task:
            messages.error(request,"Title and task cannot be empty")
        else:
            Todo.objects.create(title=title, task=task)
        return redirect('index')

class DetailView(View):
    def get(self, request,id):
        todo = Todo.objects.get(id=id)
        return render(request, 'detail_view.html', {"todo":todo})

class DeleteView(View):
    def get(self, request,id):
        todo = Todo.objects.get(id=id)
        todo.delete()
        return redirect('index')