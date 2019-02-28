from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings

# app_name = 'signup'
urlpatterns = [
    #path('apply/', views.apply, name='apply'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='signup/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='signup/logged_out.html'), name='logout'),
    path('edit/', views.update_profile, name='edit'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
        auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
        views.activate, name='activate'),
    re_path(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
]
