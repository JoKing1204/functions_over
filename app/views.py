from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse


# Create your views here.
def hey(request: HttpRequest, name) -> HttpResponse:
    return HttpResponse(f"Hey, {name}!")


def age_in(request: HttpRequest, end: int, birthyear: int) -> HttpResponse:
    return HttpResponse(end - birthyear)


def order_total(
    request: HttpRequest, burgers: float, fries: float, drinks: float
) -> HttpResponse:
    return HttpResponse((burgers * 4.5) + (fries * 1.5) + (drinks * 1))
