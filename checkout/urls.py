from django.urls import path 
from . import views

urlpatterns = [
    path('links/<str:code>',views.LinkAPIView.as_view()),
     path('orders',views.OrderAPIView.as_view())
]
