"""
Name: Nathan Dennis

Creates the manual functions for hw2 using a data set
(a list of dictionaries, specifically) labeled 'data',
which represents data for specific pokemon. This file contains
multiple functions which manipulates and answers question about
the pokemon data, such as questions regarding the atk(attack),
level, and other statistics for the pokemon within the data set.
"""

import math

import numpy as np
import pandas as pd


def species_count(data):
    """
    Counts the amount of unique pokemon species
    within this data set, returning this amount,
    using a list of dictionaries, the data variable.
    """
    unique = set()
    for i in range(len(data)):
        line = data[i]
        unique.add(line['name'])
    return len(unique)


def max_level(data):
    """
    Uses a list of dictionaries, data, to find the highest
    level pokemon in the data set, returning a
    tuple based on the name and level of the pokemon.
    If there is a tie for the pokemon with the highest level,
    meaning there is more than one pokemon with the highest level,
    the first pokemon with that level which appears in the file
    is returned.
    """
    name = None
    level = 0
    for i in range(len(data)):
        line = data[i]
        if line['level'] > level:
            name = line['name']
            level = line['level']
    return (name, level)


def filter_range(data, x, y):
    """
    Takes a range of values from x (inclusive) to
    y (exclusive) and takes pokemon within the list of
    dictionaries, data, whose level falls between this range,
    returning a list of the names of these pokemon.
    """
    pokemon = []
    for i in range(len(data)):
        line = data[i]
        if line['level'] >= x and line['level'] < y:
            pokemon.append(line['name'])
    return pokemon


def mean_attack_for_type(data, types):
    """
    Calculates the mean attack damage for a specific
    type of pokemon within the list of dictionaries, data,
    obtaining the average value for every pokemon for
    a certain type. Returns none of there are no pokemon.
    """
    total = 0
    pokemons = 0
    for i in range(len(data)):
        line = data[i]
        if line['type'] == types:
            pokemons += 1
            total = total + line['atk']
    if pokemons > 0:
        return total / pokemons
    else:
        return None


def count_types(data):
    """
    Counts the amount of different types for pokemon
    within the list of dictionaries, data, returning
    a dictionary based on how many of each type there are.
    """
    types = {}
    for i in range(len(data)):
        line = data[i]
        if line['type'] not in types:
            types[line['type']] = 1
        else:
            types[line['type']] += 1
    return types


def mean_attack_per_type(data):
    """
    Calculates the mean attack damage per type
    of pokemon within the list of dictionaries, data,
    returning a dictionary based on the mean attack
    for every type.
    """
    pokemon = {}
    counts = {}
    for i in range(len(data)):
        line = data[i]
        if line['type'] not in pokemon:
            pokemon[line['type']] = line['atk']
            counts[line['type']] = 1
        else:
            pokemon[line['type']] += line['atk']
            counts[line['type']] += 1
    for i in pokemon.keys():
        pokemon[i] = pokemon[i] / counts[i]
    return pokemon
