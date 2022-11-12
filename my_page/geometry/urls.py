
from django.urls import path
from .views import *

urlpatterns = [
    path('rectangle/<int:width>/<int:height>', get_rectangle_area),
    path('square/<int:width>/', get_square_area),
    path('circle/<int:radius>/', get_circle_area),

]
