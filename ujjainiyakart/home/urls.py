from django.urls import path,include
from . import views 

urlpatterns =[
    path('',views.index),
    path('signin',views.signin),
    path('ulogin',views.ulogin),
    path('logout',views.logout),
    path('cardpage',views.cardpage),
    path('deletecart',views.deletecart),
]

