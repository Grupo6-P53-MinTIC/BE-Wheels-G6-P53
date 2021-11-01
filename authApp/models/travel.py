from django.db import models
from django.conf import settings


class Travel(models.Model):
    id = models.AutoField(primary_key=True)
    id_manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )
    from_place = models.CharField(max_length=100)
    to_place = models.CharField(max_length=100)
    pass_through = models.CharField(max_length=100, null=True)
    published = models.DateTimeField(auto_now_add=True)
    date_travel = models.DateTimeField()
    seats = models.IntegerField(default=1)
    price = models.FloatField(default=0)
