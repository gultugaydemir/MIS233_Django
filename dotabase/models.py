from django.db import models


class WeeklyPolls(models.Model):
    answer= models.CharField(max_length=100)

    def __str__(self):
        return self.answer


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

class Buildings(models.Model):
    building_name = models.CharField(max_length=100)
    building_image = models.URLField(default="https://static.wikia.nocookie.net/dota2_gamepedia/images/5/52/Tower_Protection_icon.png/revision/latest/scale-to-width-down/128?cb=20160426211855")
    radius = models.CharField(max_length=5)
    duration = models.FloatField(max_length=6)
    ability = models.CharField(max_length=100)
    affects = models.CharField(max_length=100)

    def __str__(self):
        return self.building_name

class Events(models.Model):
    event_name = models.CharField(max_length=100)
    event_banner = models.URLField(default="https://static.wikia.nocookie.net/dota2_gamepedia/images/6/6c/Main_Page_Giant_Banner_New_Bloom_2020.jpg/revision/latest/scale-to-width-down/800?cb=20200124152923")
    event_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.event_name


