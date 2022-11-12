
from django.urls import path
from .views import *


urlpatterns = [
    path('int:<week>/', week_int),
    path('str:<week>/', week),
]
