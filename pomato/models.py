from django.db import models

# Create your models here.

class Mobiles(models.Model):
    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = 'pics')
    mob = models.CharField(max_length = 200)
    price = models.IntegerField()
    offer = models.BooleanField(default = False)
