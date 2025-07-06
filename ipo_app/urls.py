from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ipo/<int:pk>/', views.ipo_detail, name='ipo_detail'),
]
 