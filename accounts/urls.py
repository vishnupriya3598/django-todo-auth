from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('todo/', views.todo_list, name='todo'),
    path('todo/toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('todo/edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('todo/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

]
