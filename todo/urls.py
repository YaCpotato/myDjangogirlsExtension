from django.urls import path 
from . import views
from django.contrib.auth import views as v

urlpatterns = [
    path('accounts/login/', v.LoginView.as_view(), name='login'),
    path('accounts/logout/', v.LogoutView.as_view(next_page='/'), name='logout'),
    path('todo/', views.task_list, name='task_list'),
    path('todo/new/', views.task_new, name='task_new'),
    path('todo/<int:pk>/edit/', views.task_edit, name='task_edit'),

]