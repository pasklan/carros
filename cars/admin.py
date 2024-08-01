from django.contrib import admin
from .models import Car, Brand


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year',
                    'model_year', 'value', 'plate')
    search_fields = ('model',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
