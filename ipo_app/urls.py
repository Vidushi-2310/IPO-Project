from django.urls import path
from .views import home, ipo_detail, IPOListAPIView, IPODetailAPIView, admin_dashboard

urlpatterns = [
    path('', home, name='home'),
    path('ipo/<int:pk>/', ipo_detail, name='ipo_detail'),
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('api/ipo/', IPOListAPIView.as_view(), name='ipo_list_api'),
    path('api/ipo/<int:pk>/', IPODetailAPIView.as_view(), name='ipo_detail_api'),
]
