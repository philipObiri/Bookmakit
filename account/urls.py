from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # URL to the function based login view :
    # path("login/", views.user_login, name="login"),

    # URL to the Built In Login / Logout views :
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('', views.dashboard, name='dashboard'),
]
