from django.db import models

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    cellphone = models.CharField(max_length=12)
    created = models.DateTimeField(auto_now=True)
    date = models.DateField()
    is_manager = models.BooleanField(default=False)
    
