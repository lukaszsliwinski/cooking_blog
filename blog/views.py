from django.shortcuts import render
from django.db.models import Q
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
    dishes = Dish.objects.filter(kind_of_meal=category).order_by('-created_date')
    kinds_list = KINDS_LIST
    countries_list = COUNTRIES_LIST
    return render(request, 'blog/index.html', {'dishes': dishes, 'kinds_list': kinds_list, 'countries_list': countries_list})

def country(request, country):
    dishes = Dish.objects.filter(country=country).order_by('-created_date')
    kinds_list = KINDS_LIST
    countries_list = COUNTRIES_LIST
    return render(request, 'blog/index.html', {'dishes': dishes, 'kinds_list': kinds_list, 'countries_list': countries_list})

def category_diet(request, category):
    dishes = Dish.objects.filter(kind_of_meal=category, diet=True).order_by('-created_date')
    kinds_list = KINDS_LIST
    countries_list = COUNTRIES_LIST
    return render(request, 'blog/index.html', {'dishes': dishes, 'kinds_list': kinds_list, 'countries_list': countries_list})

def country_diet(request, country):
    dishes = Dish.objects.filter(country=country, diet=True).order_by('-created_date')
    kinds_list = KINDS_LIST
    countries_list = COUNTRIES_LIST
    return render(request, 'blog/index.html', {'dishes': dishes, 'kinds_list': kinds_list, 'countries_list': countries_list})

def search(request, query=""):
    dishes = Dish.objects
    if request.GET:
        query = request.GET['searchbar']
        searched_words = query.split(' ')
        for word in searched_words:
            dishes = Dish.objects.filter(Q(dish_name__icontains=word)).order_by('-created_date')
    kinds_list = KINDS_LIST
    countries_list = COUNTRIES_LIST
    return render(request, 'blog/index.html', {'dishes': dishes, 'kinds_list': kinds_list, 'countries_list': countries_list})
