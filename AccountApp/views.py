from django.shortcuts import render,redirect
from django.contrib import messages
from AccountApp.form import CustomRegisterFrom

def register(request):
    register_data = CustomRegisterFrom(request.POST)
    if register_data.is_valid():
        register_data.save()
        messages.success(request,("New user account created"))
        return redirect('register')
    else:
        register_data = CustomRegisterFrom()
    return render(request, 'register.html',{"register_data":register_data})