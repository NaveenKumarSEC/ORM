from django.db import models
class car(models.Model):
    car_id=models.IntegerField(primary_key=True)
    brand=models.CharField(max_length=30)
    model=models.CharField(max_length=30)
    year=models.DateField()
    price=models.IntegerField()