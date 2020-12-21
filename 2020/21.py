#!/usr/bin/env python
import sys
from networkx import Graph
from networkx.algorithms.bipartite.matching import maximum_matching
from collections import Counter

ingredient_counts = Counter()
allergens = {}

for line in sys.stdin.read().splitlines():
    food_ingredients, food_allergens = line.split(" (contains ")
    food_ingredients = food_ingredients.split()
    food_allergens = food_allergens[:-1].split(", ")

    ingredient_counts.update(food_ingredients)

    for allergen in food_allergens:
        if allergen in allergens:
            allergens[allergen] &= set(food_ingredients)
        else:
            allergens[allergen] = set(food_ingredients)

matching = maximum_matching(Graph(
    (ingredient, allergen)
    for allergen, ingredients in allergens.items()
    for ingredient in ingredients
))

print(sum(
    ingredient_counts[ingredient]
    for ingredient in (ingredient_counts.keys() - matching.keys())
))

print(",".join(
    matching[allergen]
    for allergen in sorted(allergens)
))