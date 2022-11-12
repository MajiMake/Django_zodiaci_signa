from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def get_rectangle_area(request, width: int, height: int):
    redirected_urls = reverse('rectangle_name', args=(width, height))
    return HttpResponseRedirect(redirected_urls)


def get_square_area(request, width: int):
    redirected_urls = reverse('square_name', args=(width,))
    return HttpResponseRedirect(redirected_urls)


def get_circle_area(request, radius: int):
    redirected_urls = reverse('circle_name', args=(radius, ))
    return HttpResponseRedirect(redirected_urls)


def rectangle(request, width: int, height: int):
    return HttpResponse(
        f'Площадь прямоугольника размером {width}x{height} равна {width * height}')


def square(requset, width: int):
    return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {width ** 2}')


def circle(request, radius: int):
    return HttpResponse(f'Площадь круга радиусом {radius} равна {3.14 * radius ** 2}')
