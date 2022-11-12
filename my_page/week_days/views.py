
from django.http import HttpResponse

week_dir = {'monday': 'Дела на понедельник',
            'tuesday': 'Дела на вторник',
            'wednesday': 'Дела на среду',
            'thursday': 'Дела на четверг',
            'friday': 'Дела на пятницу', }

week_int ={'1': 'Сегодня 1 день недели'}


def week(request, week: str):
    try:
        return HttpResponse(week_dir[week])
    except KeyError:
        return HttpResponse('Введено неверное значение')


def week_int(request, week: int):
    try:
        return HttpResponse(week_dir[week])
    except KeyError:
        return HttpResponse('Введено неверное значение')



