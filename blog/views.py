from django.shortcuts import render
from .models import Dish, KINDS_LIST, COUNTRIES_LIST

def index(request):
    dishes = Dish.objects.order_by('-created_date')
    kinds_list = KINDS_LIST
    countries_list = COUNTRIES_LIST
    return render(request, 'blog/index.html', {'dishes': dishes, 'kinds_list': kinds_list, 'countries_list': countries_list})

def details(request, dish_id):
    dish = Dish.objects.get(pk=dish_id)
    kinds_list = KINDS_LIST
    countries_list = COUNTRIES_LIST
    return render(request, 'blog/details.html', {'dish': dish, 'kinds_list': kinds_list, 'countries_list': countries_list})

def category(request, category):
    dishes = Dish.objects.filter(kind_of_meal=category)
    kinds_list = KINDS_LIST
    countries_list = COUNTRIES_LIST
    return render(request, 'blog/category.html', {'dishes': dishes, 'kinds_list': kinds_list, 'countries_list': countries_list})

def country(request, country):
    dishes = Dish.objects.filter(country=country)
    kinds_list = KINDS_LIST
    countries_list = COUNTRIES_LIST
    return render(request, 'blog/country.html', {'dishes': dishes, 'kinds_list': kinds_list, 'countries_list': countries_list})
