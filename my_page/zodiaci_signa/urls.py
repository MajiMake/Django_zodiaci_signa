
from django.urls import path
from .views import *

urlpatterns = [
    path('',)
    path('<int:sign_zodiac>/', get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', get_info_about_sign_zodiac, name='horoscope_name'),

]
