from django.http import HttpResponse


def get_rectangle_area(request, width: int, height: int):
    return HttpResponse(
        f'Площадь прямоугольника размером {width}x{height} равна {width * height}')


def get_square_area(requset, width: int):
    return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {width ** 2}')


def get_circle_area(request, radius: int):
    return HttpResponse(f'Площадь круга радиусом {radius} равна {3.14 * radius**2}')
