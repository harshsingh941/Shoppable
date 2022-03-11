import imp
import re
from unicodedata import category
from django.shortcuts import render ,redirect
from django.contrib.auth.hashers import  check_password
from numpy import product
from store.models.customer import Customer
from django.views import View
from store.models.orders import Order
from store.models.product import Product


class CheckOut(View):
    def post(self,request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer=request.session.get('customer')
        cart=request.session.get('cart')
        products=Product.get_products_by_id(list(cart.keys()))
        
        for product in products:
          order=Order(customer=Customer(id=customer),product=product,price=product.price,
                      quantity=cart.get(str(product.id)),
                      address=address,phone=phone) 
          order.save() 
        request.session['cart']={} 
        
        return redirect('cart')        