from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .forms import Todoforms
from .models import Task


def taskview(request):
    obj1=Task.objects.all()
    if request.method=="POST":
        tname=request.POST['taskname']
        tpty=request.POST['taskpty']
        tdate=request.POST['taskdate']
        obj=Task(name=tname,pty=tpty,date=tdate)
        obj.save()
    return render(request,'taskview.html',{'obj2':obj1})
class Tasklistview(ListView):
    model=Task
    template_name ='taskview.html'
    context_object_name ='obj2'

class Taskdetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'i'

class Taskupdateview(UpdateView):
    model=Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields=['name','pty','date']
    def get_success_url(self):
        return reverse_lazy('taskdetail',kwargs={'pk':self.object.id})
class Taskdeleteview(DeleteView):
    model = Task
    template_name ='delete.html'
    success_url = reverse_lazy('tasklist')





def delete(request,taskid):
    taskobj=Task.objects.get(id=taskid)
    if request.method=="POST":
        taskobj.delete()
        return redirect('/')

    return render(request,'delete.html',{'taskkey':taskobj})

def update(request,updateid):
    taskobj=Task.objects.get(id=updateid)
    formobj=Todoforms(request.POST or None,instance=taskobj)
    if formobj.is_valid():
        formobj.save()
        return redirect('/')
    return render(request,'edit.html',{'task':taskobj,'formkey':formobj})



