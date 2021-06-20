from enum import Enum
from typing import Union

from mcr.json_dict import JsonDict


class eRecipe(str, Enum):
    blasting = 'minecraft:blasting'
    campfire_cooking = 'minecraft:campfire_cooking'
    smelting = 'minecraft:smelting'
    smoking = 'minecraft:smoking'
    stonecutting = 'minecraft:stonecutting'
    crafting_shaped = 'minecraft:crafting_shaped'
    crafting_shapeless = 'minecraft:crafting_shapeless'
    crafting_special_armordye = 'minecraft:crafting_special_armordye'
    crafting_special_bannerduplicate = 'minecraft:crafting_special_bannerduplicate'
    crafting_special_bookcloning = 'minecraft:crafting_special_bookcloning'
    crafting_special_firework_rocket = 'minecraft:crafting_special_firework_rocket'
    crafting_special_firework_star = 'minecraft:crafting_special_firework_star'
    crafting_special_firework_star_fade = 'minecraft:crafting_special_firework_star_fade'
    crafting_special_mapcloning = 'minecraft:crafting_special_mapcloning'
    crafting_special_mapextending = 'minecraft:crafting_special_mapextending'
    crafting_special_repairitem = 'minecraft:crafting_special_repairitem'
    crafting_special_shielddecoration = 'minecraft:crafting_special_shielddecoration'
    crafting_special_shulkerboxcoloring = 'minecraft:crafting_special_shulkerboxcoloring'
    crafting_special_tippedarrow = 'minecraft:crafting_special_tippedarrow'
    crafting_special_suspiciousstew = 'minecraft:crafting_special_suspiciousstew'


class Result(JsonDict):
    count:	int
    item:	str


class Ingredient(JsonDict):
    item:	str
    tag:	str


def init_ingredient_or_list(json_dict: Union[dict, list[dict]]):
    if isinstance(json_dict, dict):
        return Ingredient(json_dict)
    else:
        ingredient_list = []
        for ingredient in json_dict:
            ingredient_list.append(Ingredient(ingredient))
        return ingredient_list


class Recipe(JsonDict, overrides={'type_': 'type'}):
    type_: 	eRecipe
    group: 	str


class CraftingShaped(Recipe, overrides={'key': init_ingredient_or_list}):
    pattern:	list[str]
    key:		dict[str, Union[Ingredient, list[Ingredient]]]
    result:		Result
