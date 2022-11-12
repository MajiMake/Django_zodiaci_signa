
from django.urls import path
from .views import *

urlpatterns = [
    path('int:<sign_zodiac>/', get_info_about_sign_zodiac_by_number),
    path('<sign_zodiac>/', get_info_about_sign_zodiac),

]
