from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Produits(models.Model):
    title = models.CharField(max_length=200)   
    price = models.FloatField()
    description = models.TextField()     
    image = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return self.title
        
        
