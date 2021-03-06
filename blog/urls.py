from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:dish_id>/', views.details, name='details'),
    path('category/<category>/', views.category, name='category'),
    path('country/<country>/', views.country, name='country'),
    path('search/', views.search, name='search'),
    path('category_low_calories/<category>/', views.category_low_calories, name='category_low_calories'),
    path('country_low_calories/<country>/', views.country_low_calories, name='country_low_calories')
]