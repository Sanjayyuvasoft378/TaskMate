from django.shortcuts import render,redirect
from django.http import HttpResponse
from testingapp.models import TodoListModel
from testingapp.form import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    context = {
        "welcome_text":"This is Homepage"
    }
    return render(request,'index.html', context)
@login_required
def num(request):
    if request.method =='POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            instance.save()
            messages.success(request,("New task added"))
            return redirect('num')
        else:
            messages.success(request,("please fill form properly"))
            return redirect('num')
    else: 
        all_data = TodoListModel.objects.filter(manage = request.user)
        paginator = Paginator(all_data,10)
        page = request.GET.get('pg')
        all_data = paginator.get_page(page)
        return render(request,"task.html",{ 'all_data':all_data })
@login_required
def delete_task(request,taskId):
    task = TodoListModel.objects.get(pk=taskId)
    if task.manage == request.user:
        task.delete()
    else:
        messages.success(request,("Access Restricted, You are not allowed !!"))
    return redirect('num')
@login_required
def edit_task(request,taskId):
    if request.method == "POST":
        data = TodoListModel.objects.get(pk=taskId)
        form = TaskForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
        messages.success(request,("Task Edited !!"))
        return redirect('num')
    else:
        task_data = TodoListModel.objects.get(pk = taskId)
        return render(request, 'edit.html',{'task_data':task_data})
@login_required
def Markascompleted(request, taskId):
    task_data1 = TodoListModel.objects.get(pk = taskId)
    if task_data1.manage == request.user:
        task_data1.done = True
        task_data1.save()
    else:
        messages.success(request,("Access Restricted, You are not allowed !!"))
    return redirect('num')
@login_required
def Markaspending(request, taskId):
    task_data1 = TodoListModel.objects.get(pk = taskId)
    task_data1.done = False
    task_data1.save()
    return redirect('num')


def Contact(request):
    context = {
        'welcome_text':"welcome to Contact us page"
    } 
    return render(request,"contact.html",context)


def About(request):
    context = {
        'welcome_text':"welcome to About us page"
    } 
    return render(request,"about.html",context)


def Navbar(request):
    return render(request,"nav.html")