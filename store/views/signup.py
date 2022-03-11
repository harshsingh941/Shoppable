import imp
from unicodedata import category
from django.shortcuts import render ,redirect
from django.contrib.auth.hashers import make_password 
from numpy import product
from store.models.customer import Customer
from django.views import View

class Signup(View):
    def get(self,request):
        return render(request , 'signup.html')
    def post(self,request):
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        error_message=None
        
        customer=Customer(first_name=first_name,
                          last_name=last_name,
                          phone=phone,
                          email=email,
                          password=password)
              
        
        #validation
        value={
            'first_name': first_name,
            'last_name': last_name,
            'phone':phone,
            'email':email
        }
        
                             
        error_message=self.validateCustomer(customer)         
                    
        
        #saving
        if not error_message: 
              customer=Customer(first_name=first_name,
                          last_name=last_name,
                          phone=phone,
                          email=email,
                          password=password)
              customer.password=make_password(customer.password)
              customer.register()
              return redirect('homepage')
        else:
            data= {
               'error': error_message,
               'values': value 
            }    
            return render(request,'signup.html',data)
    
    def validateCustomer(self,customer):
        error_message=None;
        if(not customer.first_name):
            error_message="First Name required!!"
        elif len(customer.first_name)<4:
           error_message="Must be least 4 characters "
        elif (not customer.last_name):
            error_message="Last Name Required!!"
        elif len(customer.last_name)<4:
            error_message="Must be least 4 characters "
        elif not customer.phone:
            error_message="Phone Number Require!!" 
        elif len(customer.phone)<9:
            error_message="Invalid Phone Number" 
        elif not customer.password:
            error_message="Enter Password!!"
        elif len(customer.password)<6 :
            error_message="Password must be least 7 characters"
        elif customer.isExists():    
            error_message="Email Address already registered"
        return error_message
 