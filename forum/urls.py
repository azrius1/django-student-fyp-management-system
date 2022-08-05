from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum, name='forumHome'),
    path('catalog/', views.catalog, name='catalog'),
    path('<str:room>', views.room, name='room'),
    path('checkview/', views.checkview, name='checkview'),
    path('send/', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]