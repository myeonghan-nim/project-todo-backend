from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.todo_create),
    path('todo/<int:todo_id>/', views.todo_detail),
    path('users/<int:user_id>/', views.user_detail),
]
