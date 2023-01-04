from django.db import models

class Booking(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=254, null=True, blank=True)
    nperson = models.PositiveSmallIntegerField(null=True, blank=True)
    comments = models.CharField(max_length=999, null=True, blank=True)
    
    def __str__(self):
        return self.name
