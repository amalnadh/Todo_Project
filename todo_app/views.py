from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Task
from .forms import Todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic import DeleteView

class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'
class Taskdetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'
class Updateview(UpdateView):
    model = Task
    template_name = 'update.html'

    context_object_name = 'task'
    fields = ('name', 'priority', 'date', 'time')
    def get_success_url(self):
        return reverse_lazy('classview')

class Deleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('classview')







# Create your views here.
def add(request):
    task1=Task.objects.all()


    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        task=Task(name=name,priority=priority,date=date,time=time)
        task.save()


    return render(request,'home.html',{'task1':task1})

# def delete(request,taskid):
#     dele=Task.objects.get(id=taskid)
#     if request.method=='POST':
#         dele.delete()
#         return redirect('/')
#
#     return render(request,'delete.html')
# def update(request,id):
#     upd=Task.objects.get(id=id)
#     frm=Todoform(request.POST or None, instance=upd)
#     if frm.is_valid():
#         frm.save()
#         return redirect('/')
#     return render(request,'update.html',{'frm':frm,'upd':upd})

