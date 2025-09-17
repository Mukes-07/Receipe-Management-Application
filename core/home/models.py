from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=99)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    image = models.ImageField()
    file = models.FileField() 

class Product(models.Model):
    pass 




class Car(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default=50)

    def _str_(self) -> str:
        return self.car_name

