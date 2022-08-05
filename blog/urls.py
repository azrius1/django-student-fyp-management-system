from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('home/', views.home, name='blog-home'),
    path('logbook/', views.logbookView.as_view(), name = 'logbook'),
    path('addlogbook/', views.AddlogbookView.as_view(), name = 'addlogbook'),
    path('lprofile/missa/', views.lprofile1, name = 'lprofile1'),
    path('lprofile/sirb/', views.lprofile2, name = 'lprofile2'),
    path('sprofile/studentc/', views.studentc, name = 'studentc'),
    path('sprofile/studentd/', views.studentd, name = 'studentd'),
]
