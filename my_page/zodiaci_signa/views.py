from django.http import HttpResponse

zodiacs = {'leo': 'Знак зодиака Лев',
           'scorpio': 'Знак зодиака Скорпион',
           'aries': 'Знак зодиака Овен',
           'taurus': 'Знак зодиака Телец',
           'libra': 'Знак зодиака Весы',
           'gemini': 'Знак зодиака Близнецы',
           'cancer': 'Знак зодиака Рак',
           'virgo': 'Знак зодиака Дева',
           'saggitarius': 'Знак зодиака Стрелец',
           'capricorn': 'Знак зодиака Козерог',
           'aquarius': 'Знак зодиака Водолей',
           'pisces': 'Знак зодиака Рыбы',
           }


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    try:
        return HttpResponse(zodiacs[sign_zodiac])
    except KeyError:
        return HttpResponse(f'Введено неверное значение - {sign_zodiac}')


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    try:
        return HttpResponse(zodiacs[sign_zodiac])
    except KeyError:
        return HttpResponse(f'Введено неверное значение - {sign_zodiac}')
