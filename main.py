import random

def run_day_trip_generator():
    destinations = ["Atlanta","Houston","Miami","Los Angeles"]
    restaurants = ["Cafe Lucia","Cafe Intermezzo","The Tavern","Maggianos"]
    transportation = ["Private Jet","Commercial Plane","Car","Bus"]
    entertainment = ["Hiking","Ziplining","Live Music","Carnival"]
    dest_option = generate_random_item(destinations)
    rest_option = generate_random_item(restaurants)
    tran_option = generate_random_item(transportation)
    enter_option = generate_random_item(entertainment)
    trip_options_list = []
    trip_options_list.append(dest_option)
    trip_options_list.append(tran_option)
    trip_options_list.append(rest_option)
    trip_options_list.append(enter_option)
    full_trip_print(trip_options_list)

def full_trip_print(options_list):
    print("Welcome to your Random Day Trip Generator, Here is your Selected Day Trip! ")
    print(f"Here is where you will be going: {options_list[0]}")
    print(f"Here is how you'll get there: {options_list[1]}")
    print(f"Here is a restaurant you should try: {options_list[2]}")
    print(f"Look out for this entertainment while you're there!: {options_list[3]}")

def generate_random_item(list_of_items):
    rand_choice = random.choice(list_of_items)
    return rand_choice

def satisfaction_generator(current_trip, trip_options):
    user_input = input("Is this to your satisfaciton? (y/n): ")
    if user_input == "n":
        print("Sorry about that, here is another option")
    else:
        print("Glad we could help!")
    





run_day_trip_generator()






