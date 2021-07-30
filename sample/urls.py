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
from django.conf import settings
from django.conf.urls.static import static

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
    path('employee_edit/', views.employee_edit, name='employee_edit'),
    path('netflix_list/', views.netflix_list, name='netflix_list'),
    path('netflix_data/', views.netflix_data, name='netflix_data'),
    path('netflix_paginate_data/',
         views.netflix_paginate_data, name='netflix_paginate_data'),
    path('netflix_paginate/', views.netflix_paginate, name='netflix_paginate'),
    path('netflix/', views.netflix, name='netflix'),
    path('planet_paginate/', views.planet_paginate, name='planet_paginate'),
    path('planet_paginate_data/', views.planet_paginate_data,
         name='planet_paginate_data'),
    path('planet_data/', views.planet_data, name='planet_data'),
    path('planet_data_display/', views.planet_data_dispaly,
         name='planet_data_display'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
