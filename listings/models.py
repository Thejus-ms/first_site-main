from django.db import models
from datetime import datetime
from realtors.models import Realtor
class Listings(models.Model):


    realtor=models.ForeignKey(Realtor,on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=50)
    zipcode=models.CharField(max_length=10)
    description=models.TextField()
    bedrooms=models.IntegerField()
    bathrooms=models.DecimalField(max_digits=2,decimal_places=1)
    garage=models.IntegerField(default=0)
    sqft=models.IntegerField()
    lot_size=models.DecimalField(max_digits=5,decimal_places=2)
    price=models.IntegerField(default=False)
    is_published=models.BooleanField(default=True)
    list_date=models.DateTimeField(default=datetime.now)
    photo_main=models.ImageField(upload_to='photos/%y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo_2 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo_3 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo_4 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo_5=models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo_6 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    def __str__(self):
        return self.title







# Create your models here.
