from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path('', views.home,name='home'),
    path('register',views.register,name='register'),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("todo/", views.todo_list, name="todo"),
    path("delete/<int:task_id>/", views.delete_task, name="delete_task"),
    path("edit/<int:task_id>/", views.edit_task, name="edit_task"),
    path("toggle/<int:task_id>/", views.toggle_task, name="toggle_task"),


]