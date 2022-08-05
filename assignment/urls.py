"""assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('forum/', include('forum.urls')),
    path('', include('blog.urls')),
    path('logbook/', blog_views.logbookView.as_view(), name = 'logbook'),
    path('addlogbook/', blog_views.AddlogbookView.as_view(), name = 'addlogbook'),
    path('appointment/', blog_views.appointment, name='appointment'),
    path('notification/', blog_views.notification, name='notification'),
    path('grade/', blog_views.grade, name='grade'),
    path('schedule/', blog_views.schedule, name='schedule'),
    path('lprofile/', blog_views.lprofile, name='lprofile'),
    path('sprofile/', blog_views.sprofile, name='sprofile'),
    path('progression/', blog_views.progression, name='progression'),
    path('chat/', include('chat.urls')),
    path('archive/', include('archive.urls')),
]
