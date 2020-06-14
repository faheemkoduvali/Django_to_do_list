
from django.urls import path
from . import views

app_name='todos'


urlpatterns = [
    path('', views.todo_list), 
    path('create/',views.todo_create),
    path('<id>/',views.Todo_details),
    path('<id>/update/',views.todo_update)

]
