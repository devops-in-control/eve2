from django.shortcuts import render, HttpResponse
from django.views import View


class Order(View):
    def get(self, request):
        return render(request, 'order/index.html')
        
        
    # handle order submission
    def post(self, request): 
        
        return render(request, 'order/index.html')