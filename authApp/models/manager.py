from django.db import models
from .user import User

class Manager(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        related_name= "manager_user",
        on_delete=models.SET_NULL,
        null=True,
    )
    car_type = models.CharField(max_length=45, choices=(
        ('sedan', 'sedan'),
        ('sedan', 'sedan'),
        ('pickup', 'pickup'),
        ('other', 'other')
    ))
    license_number = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

