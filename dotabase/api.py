import json
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse
from dotabase.models import Hero

class DOTA_API:

    def hero_parse(self):
        with open('heroes.json', encoding="utf8") as json_file:
            data = json.load(json_file)
            hero_count = 0
            for hero_index in data:
                new_hero = Hero()
                new_hero.HeroID = hero_index['HeroID']
                new_hero.name = hero_index['name']
                new_hero.primary_attribute = hero_index['attributes']['AttributePrimary']
                new_hero.attack_type = hero_index['attributes']['AttackCapabilities']
                roles = hero_index['attributes']['Role'].split(',')
                new_hero.roles = roles[0]
                hero_count = new_hero.HeroID
        return hero_count    
    
    
