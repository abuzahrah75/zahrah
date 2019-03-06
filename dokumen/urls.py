from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dokumen-index'),
   	path('testmerger', views.testmerger, name='dokumen-testmerger'),
    path('testupload', views.testupload, name='dokumen-testupload'),
	
]
