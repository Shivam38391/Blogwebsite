from django.urls import path
from . import views
from django.contrib.auth import views as authview

urlpatterns = [
    path('register/', views.register, name="register" ),
    path('login/', authview.LoginView.as_view(template_name ='users/login.html'), name='login'),
    path('logout/', authview.LogoutView.as_view(template_name ='users/logout.html'), name='logout'),
    
]