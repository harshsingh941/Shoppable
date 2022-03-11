from django.contrib import admin
from django.urls import path
from .views import home, signup , login
from .views.login import logout
from .views.home import Index,store
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView


urlpatterns = [
   path('',Index.as_view(),name='homepage'),
   path('store', store , name='store'),
   path('signup', signup.Signup.as_view(),name='signup'),
   path('login', login.Login.as_view() ,name='login'),
   path('logout', logout ,name='logout'),
   path('cart', Cart.as_view() ,name='cart'),
   path('check-out', CheckOut.as_view() ,name='checkout'),
   path('orders', OrderView.as_view() ,name='orders')
]
