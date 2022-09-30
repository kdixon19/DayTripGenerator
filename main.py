import random

def random_destination ():
    destinations = ["Atlanta","Houston","Miami","Los Angeles"]
    rand_destination = random.choice(destinations)
    return rand_destination

def random_restaurant ():
    restaurants = ["Cafe Lucia","Cafe Intermezzo","The Tavern","Maggianos"]
    rand_restaurant = random.choice(restaurants)
    return rand_restaurant

def random_transportation ():
    transportation = ["Private Jet","Commercial Plane","Car","Bus"]
    rand_transporation = random.choice(transportation)
    return rand_transporation

def random_entertainment ():
    entertainment = ["Hiking","Ziplining","Live Music","Carnival"]
    rand_entertainment = random.choice(entertainment)
    return rand_entertainment


