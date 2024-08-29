from django.db import models


class Recepie(models.Model):
    recepie_name=models.CharField(max_length=250)
    recepie_description=models.TextField()
    recepie_image=models.ImageField(upload_to="recipe")
