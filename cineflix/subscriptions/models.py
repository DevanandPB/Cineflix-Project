from django.db import models

from multiselectfield import MultiSelectField

# Create your models here.

from movies.models import BaseClass

class Devicechoices(models.TextChoices):

    ALL = 'All','All'

    PHONE = 'Phone','Phone'

    TABLET = 'Tablet','Tablet'

    TV = 'TV','TV'

    LAPTOP = 'Laptop','Laptop'

class QualityChoices(models.TextChoices):

    P480 = '480p','480p'

    P1080 = 'Upto 1080p','Upto 1080p'
    
    P4k = 'Upto 4k','Upto 4k'

class ScreenOrDownloadDeviceChoices(models.IntegerChoices):

    ONE = 1,'1'

    TWO = 2,'2'

    FOUR = 4,'4'


class SubscriptionPlans(BaseClass):

    name = models.CharField(max_length=25)

    amount = models.FloatField()

    devices = MultiSelectField(choices=Devicechoices.choices)

    quality = models.CharField(max_length=30,choices=QualityChoices.choices)

    no_of_screens = models.IntegerField(choices=ScreenOrDownloadDeviceChoices.choices)

    download_devices = models.IntegerField(choices=ScreenOrDownloadDeviceChoices.choices)

    class Meta :

        verbose_name = 'Subscription Plans'

        verbose_name_plural = 'Subscription Plans'

    def __str__(self):

        return self.name