from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render
from dataclasses import dataclass

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

@dataclass
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f'This is {self.name}'
def path_creator(request, list, path_name):
    result = ''
    zodiacs_list = list
    for sign in zodiacs_list:
        result += f'<li><a href="{sign}">{sign.title()}</a></li>'
    response = f'<ol>{result}</ol>'
    return response


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiacs.get(sign_zodiac)
    print(description)
    data = {
        'description_zodiac': description,
        'sign': sign_zodiac,
        'my_list': [1, 2, 3],
        'my_tuple': (1, 2, 3),
        'my_dict': {'name': 'Jack', 'age': 40},
        'my_int': 111,
        'my_float': 10.5,
        'my_class': Person('Will', 66)
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)



def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs_list = list(zodiacs)
    if sign_zodiac > len(zodiacs_list):
        return HttpResponseNotFound('Нифига')
    else:
        zodiac_name = zodiacs_list[sign_zodiac - 1]
        redirected_urls = reverse('horoscope_name', args=(zodiac_name,))
        return HttpResponseRedirect(redirected_urls)


def index(request):
    zodiacs_dict_list = list(zodiacs)
    context = {
        'zodiacs_dict_list': zodiacs_dict_list
    }
    return render(request, 'horoscope/index.html', context=context)


def typing(request):
    result = ''
    for sign in types_of_zadiac:
        path = reverse('types', args=(sign,))
        result += f'<li><a href="{path}">{sign.title()}</a></li>'
        response = f'<ol>{result}</ol>'
    return HttpResponse(response)


def chosen_one(request, typess):
    result = ''
    for sign_type in types_of_zadiac[typess]:
        print(types_of_zadiac[typess])
        path = reverse('horoscope_name', args=(sign_type,))
        result += f'<li><a href={path}>{sign_type.title()}</a></li>'
        response = f'<ol>{result}</ol>'
        print(response)
    return HttpResponse(response)


def get_date(request, month: int, day: int):
    last_day_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    if month not in last_day_month or day > last_day_month[month]:
        print(last_day_month[month], day)
        return HttpResponseNotFound('Неверная дата')
    else:
        if month == 1:
            if day in range(1, 20):
                return HttpResponse(zodiacs['capricorn'])

            else:
                return HttpResponse(zodiacs['pisces'])

        elif month == 2:
            if day in range(1, 20):
                return HttpResponse(zodiacs['pisces'])

            else:
                return HttpResponse(zodiacs['aquarius'])

        elif month == 3:
            if day in range(1, 21):
                return HttpResponse(zodiacs['aquarius'])

            else:
                return HttpResponse(zodiacs['aries'])

        elif month == 4:
            if day in range(1, 20):
                return HttpResponse(zodiacs['aries'])

            else:
                return HttpResponse(zodiacs['taurus'])

        elif month == 5:
            if day in range(1, 21):
                return HttpResponse(zodiacs['taurus'])

            else:
                return HttpResponse(zodiacs['gemini'])

        elif month == 6:
            if day in range(1, 21):
                return HttpResponse(zodiacs['gemini'])
            else:
                return HttpResponse(zodiacs['cancer'])
        elif month == 7:
            if day in range(1, 23):
                return HttpResponse(zodiacs['cancer'])
            else:
                return HttpResponse(zodiacs['leo'])
        elif month == 8:
            if day in range(1, 23):
                return HttpResponse(zodiacs['leo'])
            else:
                return HttpResponse(zodiacs['virgo'])
        elif month == 9:
            if day in range(1, 23):
                return HttpResponse(zodiacs['virgo'])
            else:
                return HttpResponse(zodiacs['libra'])
        elif month == 10:
            if day in range(1, 24):
                return HttpResponse(zodiacs['libra'])
            else:
                return HttpResponse(zodiacs['scorpio'])
        elif month == 11:
            if day in range(1, 23):
                return HttpResponse(zodiacs['scorpio'])
            else:
                return HttpResponse(zodiacs['saggitarius'])
        elif month == 12:
            if day in range(1, 22):
                return HttpResponse(zodiacs['saggitarius'])
            else:
                return HttpResponse(zodiacs['capricorn'])
