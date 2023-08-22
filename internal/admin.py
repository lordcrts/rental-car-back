from django.contrib import admin

from internal.models import Brand, Car, Specification, State

# Register your models here.
@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    """State model admin."""

    list_display = (
        'name',
    )
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """Brand model admin."""

    list_display = (
        'name',
    )
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    """Car model admin."""

    list_display = (
        'model',
    )
    search_fields = ('model',)
    list_filter = ('model',)

@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    """Specification model admin."""

    list_display = (
        'car',
        'maker',
    )
    search_fields = ('car__model',)
    list_filter = ('car__model',)