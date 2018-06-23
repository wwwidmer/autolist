from django.db import models


class Vehicle(models.Model):
    '''
    Representation of one Vehicle
    Vehicles (and most of their other data) are obtained from an external API
    
    VINs are standardized to be between 11-17 characters
    Vehicles can have page_views
    '''
    vin = models.CharField(max_length=17, primary_key=True)
    page_views = models.IntegerField(default=0)