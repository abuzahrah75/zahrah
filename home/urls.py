from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home-index"),
    path('testmerger',views.testmerger, name='home-testmerger'),
    path('mykat', views.show_kategori, name='home-kategori'),

]
