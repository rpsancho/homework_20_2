from django.urls import path
from catalog.views import *


urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('products/<int:pk>/', product),
]
