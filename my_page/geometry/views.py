from django.http import HttpResponse, HttpResponseRedirect


def get_rectangle_area(request, width: int, height: int):
    return HttpResponseRedirect(f'/calculate_geometry/rectangle/{width}/{height}')
def get_square_area(requset, width: int):
    return HttpResponseRedirect(f'/calculate_geometry/square/{width}')


def get_circle_area(request, radius: int):
    return HttpResponseRedirect(f'/calculate_geometry/circle/{radius}')


def rectangle(request, width: int, height: int):
    return HttpResponse(
        f'Площадь прямоугольника размером {width}x{height} равна {width * height}')

def square(requset, width: int):
    return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {width ** 2}')

def circle(request, radius: int):
    return HttpResponse(f'Площадь круга радиусом {radius} равна {3.14 * radius**2}')
