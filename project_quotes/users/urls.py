from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'  # Define the app namespace

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    # Add other URL patterns as needed
]