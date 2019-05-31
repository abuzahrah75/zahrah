from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='contacts-index'),
   	path('mycontact/list/', views.Mycontact_list.as_view(), name='mycontact-list'),
    path('mycontact/create/', views.Mycontact_create.as_view(),
         name='mycontact-create'),
    path('mycontact/update/<int:pk>',
         views.Mycontact_update.as_view(), name='mycontact-update'),
    #path('mycontact/detail/<int:pk>',views.Mycontact_detail.as_view(), name='mycontact-detail'),
    path('mycontact/detail/<int:pk>', views.mycontact_detail, name='mycontact-detail'),
    path('mycontact/delete/<int:pk>',
         views.Mycontact_delete.as_view(), name='mycontact-delete'),
    
    path('myphone/list/<int:pk>', views.myphone_list,name='myphone-list'),
    #path('myphone/create/<int:pk>', views.MyPhone_create.as_view(),name='myphone-create'),
    path('myphone/create/<int:pk>',
         views.myphone_create, name='myphone-create'),
    path('myphone/update/<int:pk>/<int:pid>',views.myphone_update, name='myphone-update'),
    path('myphone/delete/<int:pk>/<int:pid>',views.myphone_delete, name='myphone-delete'),
    path('myemail/create/<int:pk>',
         views.myemail_create, name='myemail-create'),
    path('myemail/update/<int:pk>/<int:pid>',
         views.myemail_update, name='myemail-update'),
    path('myemail/delete/<int:pk>/<int:pid>',
         views.myemail_delete, name='myemail-delete'),
    path('myaddress/create/<int:pk>',
         views.myaddress_create, name='myaddress-create'),
    path('myaddress/update/<int:pk>/<int:pid>',
         views.myaddress_update, name='myaddress-update'),
    path('myaddress/delete/<int:pk>/<int:pid>',
         views.myaddress_delete, name='myaddress-delete'),
    path('myemail/list/<int:pk>', views.myemail_list, name='myemail-list'),
    path('myaddress/list/<int:pk>', views.myaddress_list, name='myaddress-list'),

]
