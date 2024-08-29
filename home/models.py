from django.db import models

class student(models.Model):
    # id=models.AutoField()
    name=models.CharField(max_length=100)

    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    hobbies=models.TextField(null=True,blank=True)

class cars(models.Model):
    car_name=models.CharField(max_length=500)
    speed=models.IntegerField()
    def __str__(self) -> str:
        return self.car_name
# Create your models here.


class Recepie(models.Model):
    recepie_name=models.CharField(max_length=250)
    recepie_description=models.TextField()
    recepie_image=models.ImageField(upload_to="recipe")
