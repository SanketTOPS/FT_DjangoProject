from django.contrib import admin
from django.urls import path
from myshop import views

urlpatterns = [
   path('',views.index),
   path('cart/',views.cart),
   path('checkout/',views.checkout),
   path('contact/',views.contact),
   path('detail/',views.detail),
   path('shop/',views.shop),
]
