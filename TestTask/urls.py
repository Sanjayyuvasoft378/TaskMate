
from django.contrib import admin
from django.urls import path,include
from testingapp import views as task_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testapp/',include('testingapp.urls')),
    path('account/',include('AccountApp.urls')),

    path('',task_view.index,name='index'),
    path('contact/',task_view.Contact,name='contact'),
    path('about/',task_view.About,name='about'),
]
