from django.urls import path
from order.views import Order

app_name = 'order'

urlpatterns = [
    path('', Order.as_view(), name="order"),
]
