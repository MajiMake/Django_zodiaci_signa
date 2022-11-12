
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

week_dir = {'monday': 'Дела на понедельник',
            'tuesday': 'Дела на вторник',
            'wednesday': 'Дела на среду',
            'thursday': 'Дела на четверг',
            'friday': 'Дела на пятницу', }



def week_str(request, week_str: str):
    try:
        return HttpResponse(week_dir[week_str])
    except KeyError:
        return HttpResponse('Введено неверное asd')


def week_int(request, week_int: int):
    week_list = list(week_dir)
    if week_int > len(week_list):
        return HttpResponseNotFound('Fuck off')
    else:
        weekday = week_list[week_int-1]
        return HttpResponseRedirect(f'/todo_week/{weekday}')




