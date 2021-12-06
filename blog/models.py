from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

KINDS_LIST = ['I śniadanie',
            'II śniadanie',
            'obiad',
            'deser',
            'kolacja',
            'przekąska',
            ]

COUNTRIES_LIST = ['Francja',
                'Gruzja',
                'Grecja',
                'Hiszpania',
                'Indie',
                'Tajlandia',
                'INNE',
                ]

UNITS_LIST =['',
            'szt.',
            'ml',
            'l',
            'g',
            'dag',
            'kg',
            ]

KINDS_CHOICES = []
COUNTRIES_CHOICES = []
UNITS_CHOICES = []

for i in range(len(KINDS_LIST)):
    KINDS_CHOICES.append((KINDS_LIST[i], KINDS_LIST[i]))

for i in range(len(COUNTRIES_LIST)):
    COUNTRIES_CHOICES.append((COUNTRIES_LIST[i], COUNTRIES_LIST[i]))

for i in range(len(UNITS_LIST)):
    UNITS_CHOICES.append((UNITS_LIST[i], UNITS_LIST[i]))


class MinMaxFloat(models.FloatField):
    """ FloatField class with limits of values. """
    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        super(MinMaxFloat, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value' : self.max_value}
        defaults.update(kwargs)
        return super(MinMaxFloat, self).formfield(**defaults)


class Dish(models.Model):
    dish_name = models.CharField(max_length=100)
    recipe = models.TextField()
    dish_image = models.ImageField(blank=True, null=True, upload_to='images/')
    created_date = models.DateTimeField(default=timezone.now)
    kind_of_meal = models.CharField(max_length=30, default=None, choices=KINDS_CHOICES)
    country = models.CharField(max_length=30, default=None, choices=COUNTRIES_CHOICES)
    low_calories = models.BooleanField(default=True)

    def __str__(self):
        return self.dish_name


class Ingredient(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=50)
    quantity = MinMaxFloat(min_value=0.0, blank=True, null=True, default=None)
    unit = models.CharField(max_length=30, blank=True, default=None, choices=UNITS_CHOICES)

    def __str__(self):
        return self.ingredient


class Spice(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    spice = models.CharField(max_length=50)

    def __str__(self):
        return self.spice