"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('profile/',
         views.get_user_profile, name='user_profile'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('verify_email/', views.verify_email, name='verify_email'),
    path('employee_new/', views.employee_new, name='employee_new'),
    path('login/', views.login, name='login'),
    path('employee_home/', views.employee_home, name='employee_home'),
    path('employee_edit/', views.employee_edit, name='employee_edit')
]
