from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="projek-index"),
    #path('testmerger', views.testmerger, name='home-testmerger'),

]
