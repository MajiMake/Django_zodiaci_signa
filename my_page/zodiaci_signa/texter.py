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
    'fire': ('aries', 'leo', 'saggitarius'),
    'air': ('libra', 'aquarius', 'gemini'),
    'water': ('cancer', 'scorpio', 'pisces')

}


def path_creator(request, list, path_name):
    result = ''
    zodiacs_list = list
    for sign in zodiacs_list:
        result += f'<li><a href="{sign}">{sign.title()}</a></li>'
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
    response = path_creator(request, zodiacs, path_name=reverse('home'))
    return HttpResponse(response)


def typing(request):
    result = ''
    for sign in types_of_zadiac:
        path = reverse('types', args=(sign,))
        result += f'<li><a href="{path}">{sign.title()}</a></li>'
        response = f'<ol>{result}</ol>'
    return HttpResponse(response)

def chosen_one(request, typess):
    result=''
    for sign_type in types_of_zadiac[typess]:
        print(types_of_zadiac[typess])
        path = reverse('horoscope_name', args=(sign_type, ))
        result += f'<li><a href={path}>{sign_type.title()}</a></li>'
        response = f'<ol>{result}</ol>'
        print(response)
    return HttpResponse(response)

def get_date(request, month: int, day: int):
    last_day_month = {
        1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31
    }
    if month not in last_day_month or day > last_day_month[month]:
        print(last_day_month[month], day)
        return HttpResponseNotFound('Неверная дата')
    else:
        return HttpResponse('Пушка')

class sign_of_zodiac:

    def __init__(self, name):
        self.name = name
        self.sign, self.element = self.get_element()
        self.type_dir = {
            'earth': ('capricorn', 'taurus', 'virgo'),
            'fire': ('aries', 'leo', 'saggitarius'),
            'air': ('libra', 'aquarius', 'gemini'),
            'water': ('cancer', 'scorpio', 'pisces')
        }
        self.zodiac_list = {
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

    def get_element(self):
        if self.name in  self.zodiac_list:
            sign = self.name
            for element in self.type_dir:
                if self.name in self.type_dir[element]:
                    return sign, element
                else:
                    continue

        else:
            return ('Нет такого')



