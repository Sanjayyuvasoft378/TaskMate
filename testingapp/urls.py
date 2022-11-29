from django.urls import path
from testingapp import views
urlpatterns =[
    path("home/",views.num, name="num"),
    path('delete/<taskId>',views.delete_task,name='delete_task'),
    path('edit/<taskId>',views.edit_task,name='edit_task'),
    path('Markascompleted/<taskId>',views.Markascompleted,name='Markascompleted'),
    path('Markaspending/<taskId>',views.Markaspending,name='Markaspending'),
]