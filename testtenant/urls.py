from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="cuba-index"),
    #path("users/", UserCreate.as_view(), name="user_create"),
    
]
