from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),

    path('two/', views.two, name='two'),
    path('userprofile/', views.userprofile, name='userprofile'),
    path('log/', views.login, name='login'),
    path('edit/', views.edit, name='edit'),

    path('sign/', views.sign, name='sign'),
    path('sign/log/', views.log, name='log'),

    path('sign', views.handleSignUp, name='handleSignup'),
    path('sign/handleSignUp', views.handleSignUp, name='handleSignup'),

    path('handleLogin', views.handleLogin, name="handleLogin"),
    # path('login/login/', views.handleLogin, name="handleLogin"),
    # path('handleLogin', views.login, name='login'),

    path('logout', views.handleLogout, name="handleLogout"),
    path('userprofile/logout', views.handleLogout, name="handleLogout"),

]
