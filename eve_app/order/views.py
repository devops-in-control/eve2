from django.shortcuts import render, HttpResponse
from django.views import View
from .validator import *

class Order(View):
    def get(self, request):
        return render(request, 'order/index.html')
        
    # handle order submission
    def post(self, request): 
       
        # try to validate phone number
        phone_number_is_valid = None
        try:
            # validate_phone_number returns True for valid numbers and False for invalid
            phone_number_is_valid = is_valid_phone_number(request.POST['phone_number'])
        except:
            # ignore this
            phone_number_is_valid = False
  
        # if phone number is invalid, return user to order form with error message
        if phone_number_is_valid is not True:
            return render(request, \
                'order/index.html', \
                { 
                    'invalid_phone_number': True
                })
        
        # process validate phone number
        return render(request, 'order/success.html')
    