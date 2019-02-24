from django.urls import path
from django.contrib.auth import views as auth_views

# from accounts.views import register

app_name = 'account'

urlpatterns = [
    # path('register/', register, name='register'),
    path('logout/', auth_views.LogoutView.as_view, {'next_page': '/'}, name='logout'),
    path('login/', auth_views.LoginView.as_view, {'template_name': 'accounts/login.html'}, name='login'),
]
