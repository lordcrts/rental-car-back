from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
# Extras
from autoslug import AutoSlugField


class State(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=45)
    create_at = models.DateTimeField(verbose_name=_('Create at'), auto_now_add=True)
    update_at = models.DateTimeField(verbose_name=_('Update at'), auto_now=True, )

    def __str__(self):
        """Return State's str representation."""
        return str(self.name)

class Brand(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=45)
    url_slug = AutoSlugField(verbose_name=_('Slug'), max_length=50, populate_from='name', unique=True)
    create_at = models.DateTimeField(verbose_name=_('Create at'), auto_now_add=True)
    update_at = models.DateTimeField(verbose_name=_('Update at'), auto_now=True, )
    state = models.ForeignKey(State, on_delete=models.CASCADE, default=1, verbose_name=_('State'))
    

    def __str__(self):
        """Return Brand's str representation."""
        return str(self.name)

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'))
    model = models.CharField(verbose_name=_('Model'), max_length=45)
    url_slug = AutoSlugField(verbose_name=_('Slug'), max_length=50, populate_from='model', unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=1, verbose_name=_('Brand'))
    description = models.TextField(verbose_name=_('Description'))
    year = models.IntegerField(verbose_name=_('Year'))
    price = models.BigIntegerField(verbose_name=_('Price'))
    image = models.ImageField(_('Photo'), max_length=500)
    create_at = models.DateTimeField(verbose_name=_('Create at'), auto_now_add=True)
    update_at = models.DateTimeField(verbose_name=_('Update at'), auto_now=True, )
    state = models.ForeignKey(State, on_delete=models.CASCADE, default=1, verbose_name=_('State'))

    def __str__(self):
        """Return Car's str representation."""
        return str(self.url_slug)
    
class Specification(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE, verbose_name=_('Car'))
    maker = models.CharField(verbose_name=_('Maker'), max_length=45)
    identification_number = models.CharField(verbose_name=_('Identification Number'), max_length=45)
    height = models.IntegerField(verbose_name=_('Height'))
    widht = models.IntegerField(verbose_name=_('Widht'))
    longitude = models.IntegerField(verbose_name=_('Longitude'))
    km = models.IntegerField(verbose_name=_('KM'))
    create_at = models.DateTimeField(verbose_name=_('Create at'), auto_now_add=True)
    update_at = models.DateTimeField(verbose_name=_('Update at'), auto_now=True, )
    state = models.ForeignKey(State, on_delete=models.CASCADE, default=1, verbose_name=_('State'))

    def __str__(self):
        """Return Specification's str representation."""
        return str(self.car.url_slug)
