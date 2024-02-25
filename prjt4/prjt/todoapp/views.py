from django.shortcuts import render, redirect
from .models import Task
from .forms import Todoform
from django.views.generic import ListView

class listview(ListView):
    model=Task
    template_name='home.html'
    context_object_name='task1'

# Create your views here.
def home(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    return render(request, 'home.html', {'task1': task1})


def delete(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
        task = Task.objects.get(id=id)
        f = Todoform(request.POST or None, instance=task)
        if f.is_valid():
            f.save()
            return redirect('/')
        return render(request, 'edit.html', {'f': f, 'task': task})

# def details(request):
#   task=Task.objects.all()
#    return render(request,'detail.html')
