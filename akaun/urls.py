from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='akaun-index'),
   	#path('testmerger', views.testmerger, name='dokumen-testmerger'),
    #path('testupload', views.testupload, name='dokumen-testupload'),
    #path('testupload2', views.testupload2, name='dokumen-testupload2'),
	
]
