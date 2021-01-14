from django.db import models


class Heroes(models.Model):
    name = models.CharField(max_length=100)
    strength = models.CharField(max_length=3)
    agility = models.CharField(max_length=3)
    intelligence = models.CharField(max_length=3)
    image = models.URLField(default="https://static.wikia.nocookie.net/dota2_gamepedia/images/7/7a/Strength_attribute_symbol.png/revision/latest/scale-to-width-down/40?cb=20180323111829", max_length=300)

<<<<<<< HEAD
<<<<<<< HEAD
    def _str_(self):
        return self.name
=======

class Hero(models.Model):
    heroID = models.IntegerField()
    name = models.CharField(max_length=50)
    team = models.CharField(max_length=30) #radiand or dire
    primary_attribute = models.CharField(max_length=50) #agi int or str
    attack_type = models.CharField(max_length=10) #ranged or melee
    roles = models.CharField(max_length=200) #carry, support, escape, ganker, etc.
    abilities = {
        "abilityName" : models.CharField(max_length=100),
        "description" : models.CharField(max_length=300)
    }
    baseAgility = models.IntegerField()
    baseStrength = models.IntegerField()
    baseIntelligence = models.IntegerField()
    AgilityGain = models.FloatField()
    StrengthGain = models.FloatField()
    IntelligenceGain = models.FloatField()
    ArmorPhysical = models.FloatField()
    StatusHealth = models.IntegerField()
    StatusHealthRegen = models.FloatField()
    StatusMana = models.IntegerField()
    StatusManaRegen = models.FloatField()
    AttackDamage = models.IntegerField()
    AttackRange = models.IntegerField()
    Complexity = models.IntegerField()
    MovementSpeed = models.IntegerField()


class Item(models.Model):
    name = models.CharField(max_length=50)
    isPassive = models.BinaryField()   
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    
    
>>>>>>> b4753aacddd4250863225c73468441af0ede37a8
=======
    def _str_(self):
        return self.name
>>>>>>> 237bdc1d9b097164113d58d3185e703f3349942c
