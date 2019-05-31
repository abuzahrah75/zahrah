from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='invoice-index'),
   	path('list/', views.invoice_list, name='invoice-list'),
    path('detail/<int:pk>', views.invoice_detail, name='invoice-detail'),

]
