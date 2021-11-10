from django.urls import path
from . import  views
urlpatterns =[
    path('views/', views.req, name='req'),
    path('templates/', views.req1, name='req1'),
]