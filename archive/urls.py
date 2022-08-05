from django.urls import path

from . import views

# app_name = 'archive'
urlpatterns = [
    path('page1', views.uploadPage, name='uploadPage'),
    path('page2', views.archiveList, name='archiveList'),
]