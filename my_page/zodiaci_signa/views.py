from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

zodiacs = {
    'aries': 'Знак зодиака Овен',
    'taurus': 'Знак зодиака Телец',
    'gemini': 'Знак зодиака Близнецы',
    'cancer': 'Знак зодиака Рак',
    'leo': 'Знак зодиака Лев',
    'virgo': 'Знак зодиака Дева',
    'libra': 'Знак зодиака Весы',
    'scorpio': 'Знак зодиака Скорпион',
    'saggitarius': 'Знак зодиака Стрелец',
    'capricorn': 'Знак зодиака Козерог',
    'aquarius': 'Знак зодиака Водолей',
    'pisces': 'Знак зодиака Рыбы',
}


def horoscope
def get_info_about_sign_zodiac(request, sign_zodiac: str):
    try:
        return HttpResponse(zodiacs[sign_zodiac])
    except KeyError:
        return HttpResponse(f'Введено неверное значение - {sign_zodiac}')


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs_list = list(zodiacs)
    if sign_zodiac > len(zodiacs_list):
        return HttpResponseNotFound('Нифига')
    else:
        zodiac_name = zodiacs_list[sign_zodiac - 1]
        redirected_urls = reverse('horoscope_name', args=(zodiac_name,))
        return HttpResponseRedirect(redirected_urls)
