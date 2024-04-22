from django.db import models

# Create your models here.
class ItemList(models.Model):
    recipie = models.TextField() 
    comment = models.TextField()