from django.urls import path 
from . import views
from django.contrib.auth import views as v

urlpatterns = [
    path('accounts/login/', v.LoginView.as_view(), name='login'),
    path('accounts/logout/', v.LogoutView.as_view(next_page='/'), name='logout'),
    path('', views.task_list, name='task_list'),
]