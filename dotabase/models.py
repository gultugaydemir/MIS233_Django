from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


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
    
    
