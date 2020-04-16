"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from mysite.core import views

urlpatterns = [
	path('', views.home, name='home'),
	path('signup/', views.signup, name='signup'),
    path('convert/', views.temp_convert, name='convert'),
	path('calc/', views.calculator, name='calc'),
    path('pass/', views.password, name='pass'),
    path('count/', views.count, name='count'),
    path('guess/', views.guess, name='guess'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
