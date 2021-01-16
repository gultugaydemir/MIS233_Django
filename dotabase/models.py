from django.db import models


class Heroes(models.Model):
    name = models.CharField(max_length=100)
    strength = models.CharField(max_length=3)
    agility = models.CharField(max_length=3)
    intelligence = models.CharField(max_length=3)
    image = models.URLField(default="https://static.wikia.nocookie.net/dota2_gamepedia/images/7/7a/Strength_attribute_symbol.png/revision/latest/scale-to-width-down/40?cb=20180323111829", max_length=300)

    def __str__(self):
        return self.name

class Items(models.Model):
    item_name = models.CharField(max_length=100)
    item_image = models.URLField(default="https://static.wikia.nocookie.net/dota2_gamepedia/images/f/f6/Observer_Ward_icon.png/revision/latest/scale-to-width-down/100?cb=20160530171901")
    cost = models.CharField(max_length=3)
    bought_from = models.CharField(max_length=30)
    initial_stock = models.CharField(max_length=3)
    max_stock = models.CharField(max_length=3)
    restock_time = models.CharField(max_length=3)
    charges = models.CharField(max_length=3)
    disassemble = models.BooleanField()
    alert_allies = models.BooleanField()

    def __str__(self):
        return self.item_name
