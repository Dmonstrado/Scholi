from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('view/<int:pk>/', views.view, name='view'),
    path('pesquisa/', views.pesquisa, name='pesquisa'),
    path('favoritos/', views.favoritos, name='favoritos'),
    path('fav/<int:pk>/', views.fav, name='fav'),
    path('report/<int:pk>/', views.report, name='report'),
]