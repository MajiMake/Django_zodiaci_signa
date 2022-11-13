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
types_of_zadiac = {
    'earth': ('capricorn', 'taurus', 'virgo'),
    'fire': ('aries', 'lion', 'saggitarius'),
    'air': ('libra', 'aquarius', 'gemini'),
    'water': ('cancer', 'scorpio', 'pisces')

}


def path_creator(request, list, path_name, args=True):
    result = ''
    zodiacs_list = list
    for sign in zodiacs_list:
        if args is False:
            redirected_path = reverse(path_name)
        else:
            redirected_path = reverse(path_name, args=sign)
        result += f'<li><a href="{redirected_path}">{sign.title()}</a></li>'
    response = f'<ol>{result}</ol>'
    return response


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

def index(request):
    response = path_creator(request, zodiacs, 'horoscope_name')
    return HttpResponse(response)


def typing(request):
    response = path_creator(request, list=types_of_zadiac, path_name='type')
    return HttpResponse(response)


def chosen_one(request, types):
    result = []
    for sign_type in types_of_zadiac[types]:
        result.append(sign_type)
    response = path_creator(request=request, list=result, path_name='path_to_type', args=True)
    return HttpResponse(response)
