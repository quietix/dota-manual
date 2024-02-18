from django.db import models


# Create your models here.

class Hero(models.Model):
    hero_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.hero_name}'


class Build(models.Model):
    hero_name = models.ForeignKey(Hero, on_delete=models.CASCADE)
    build_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.hero_name}'
