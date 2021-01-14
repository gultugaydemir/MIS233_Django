from django.db import models


class Heroes(models.Model):
    name = models.CharField(max_length=100)
    strength = models.CharField(max_length=3)
    agility = models.CharField(max_length=3)
    intelligence = models.CharField(max_length=3)

    def __str__(self):
        return self.name