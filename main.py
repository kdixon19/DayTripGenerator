import random

def run_day_trip_generator():
    destinations = ["Atlanta","Houston","Miami","Los Angeles"]
    restaurants = ["Cafe Lucia","Cafe Intermezzo","The Tavern","Maggianos"]
    transportation = ["Private Jet","Commercial Plane","Car","Bus"]
    entertainment = ["Hiking","Ziplining","Live Music","Carnival"]
    print("Welcome to your Random Day Trip Generator, Here is your Selected Day Trip! ")
    print(f"Here is where you will be going: {generate_random_item(destinations)}")
    print(f"Here is how you'll get there: {generate_random_item(transportation)}")
    print(f"Here is a restaurant you should try: {generate_random_item(restaurants)}")
    print(f"Look out for this entertainment while you're there!: {generate_random_item(entertainment)}")


def generate_random_item(list_of_items):
    rand_choice = random.choice(list_of_items)
    return rand_choice



run_day_trip_generator()




