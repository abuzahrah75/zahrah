from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='folder-index'),
   	path('create/', views.folder_create, name='folder-create'),
	
]
