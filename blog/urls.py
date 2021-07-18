from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:dish_id>/', views.details, name='details'),
    path('category/<category>/', views.category, name='category'),
    path('country/<country>/', views.country, name='country'),
    path('search/', views.search, name='search'),
    path('category_diet/<category>/', views.category_diet, name='category_diet'),
    path('country_diet/<country>/', views.country_diet, name='country_diet')
]