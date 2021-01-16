from django.db import models


class Heroes(models.Model):
    name = models.CharField(max_length=100)
    strength = models.CharField(max_length=3)
    agility = models.CharField(max_length=3)
    intelligence = models.CharField(max_length=3)
    image = models.URLField(default="https://static.wikia.nocookie.net/dota2_gamepedia/images/7/7a/Strength_attribute_symbol.png/revision/latest/scale-to-width-down/40?cb=20180323111829", max_length=300)

    def _str_(self):
        return self.name
