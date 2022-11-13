
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('type', typing, name='type'),
    path('type/<typess>', chosen_one, name='types'),
    path('<int:sign_zodiac>', get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>', get_info_about_sign_zodiac, name='horoscope_name'),
    path('<int:month>/<int:day>', get_date, name='date')
]
