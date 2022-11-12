
from django.urls import path
from .views import *


urlpatterns = [
    path('<int:week_int>/', week_int),
    path('<week_str>/', week_str, name='week_name'),
]
