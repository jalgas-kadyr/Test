from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('', views.feed, name='feed'),
    path('registration', views.registration, name='registration'),
    path('list', views.list, name='list'),
    path('<int:user_id>/', views.user_detail, name='detail'),
]
