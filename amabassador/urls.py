from django.urls import path,include
from . import views


urlpatterns =[
    path('',include('common.urls')),
    path('products/frontend',views.ProductFrontEndApi.as_view()),
    path('products/backend',views.ProductBackendApi.as_view()),
    path('links',views.LinkAPIView.as_view()),
    path('stats',views.StatsAPIView.as_view()),
    path('rankings',views.StatsAPIView.as_view()),
]