from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='pelanggan-index'),
    path('detail/<int:pk>/', views.details, name='pelanggan-details'),
	
	
]
