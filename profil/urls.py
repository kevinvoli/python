from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='accueil' ),
    path('inscription/', views.inscription, name='inscription'),
    path('profil/',views.profil, name="profil"),
    path('login/',views.login, name="connection"),
    path('course/',views.course, name="course"),
    path('logout/',views.deconnection, name="logout"),   
]