
from django.http import HttpResponse

week_dir = {'monday': 'Дела на понедельник',
            'tuesday': 'Дела на вторник',
            'wednesday': 'Дела на среду',
            'thursday': 'Дела на четверг',
            'friday': 'Дела на пятницу', }

week_integer ={1: 'Сегодня 1 день недели',
           2: 'Сегодня 2 день недели',
           3: 'Сегодня 3 день недели',
           4: 'Сегодня 4 день недели',
           5: 'Сегодня 5 день недели',
           6: 'Сегодня 6 день недели',
           7: 'Сегодня 7 день недели',
           }


def week_str(request, week_str: str):
    try:
        return HttpResponse(week_dir[week_str])
    except KeyError:
        return HttpResponse('Введено неверное asd')


def week_int(request, week_int: int):
    try:
        return HttpResponse(week_integer[week_int])
    except KeyError:
        return HttpResponse('Неверный день недели')



