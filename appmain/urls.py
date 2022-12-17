from django.urls import path
from django.contrib.auth import views

from .views import index, signup, myaccount, edit_myaccount, shop
from appproduct.views import product

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LogoutView.as_view(template_name='appmain/login.html'), name='login'),
    path('myaccount/', myaccount, name='myaccount'),
    path('edit_myaccount/', edit_myaccount, name='edit_myaccount'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),
]