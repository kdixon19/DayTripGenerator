import random

print("Welcome to your Random Day Trip Generator!")

def master_generator_function():
    satisfaction_confirm = False
    dest_list = ["Atlanta","Houston","Miami","Los Angeles"]
    rest_list = ["Cafe Lucia","Cafe Intermezzo","The Tavern","Maggianos"]
    tran_list = ["Private Jet","Commercial Plane","Car","Bus"]
    enter_list = ["Hiking","Ziplining","Live Music","Carnival"]
    dest_option = generate_random_item(dest_list)
    rest_option = generate_random_item(rest_list)
    tran_option = generate_random_item(tran_list)
    enter_option = generate_random_item(enter_list)
    current_trip = [dest_option,tran_option,rest_option,enter_option]
    full_trip_print(current_trip)
    satisfaction_confirm = satisfaction_generator()
    while satisfaction_confirm == False:
        unwanted_input = input("Sorry to hear that, what would you like to change? The Destination, Restaurant, Transport, or Entertainment?: ")
        if unwanted_input == "Destination" or unwanted_input == "destination":
            dest_list = remove_items_from_list(dest_list, dest_option)
            dest_option = generate_random_item(dest_list)
        elif unwanted_input == "Restaurant" or unwanted_input == "restaurant":
            rest_list = remove_items_from_list(rest_list, rest_option)
            rest_option = generate_random_item(rest_list)
        elif unwanted_input == "Transportation" or unwanted_input == "transportation":
            tran_list = remove_items_from_list(tran_list, tran_option)
            tran_option = generate_random_item(tran_list)
        elif unwanted_input == "Entertainment":
            enter_list = remove_items_from_list(enter_list, enter_option)
            enter_option = generate_random_item(enter_list)
        current_trip = [dest_option, tran_option, rest_option, enter_option]
        full_trip_print(current_trip)
        satisfaction_confirm = satisfaction_generator


#This prints my trip list depending on what list I send through
def full_trip_print(options_list):
    print("Here is your Selected Day Trip! ")
    print(f"Here is where you will be going: {options_list[0]}")
    print(f"Here is how you'll get there: {options_list[1]}")
    print(f"Here is a restaurant you should try: {options_list[2]}")
    print(f"Look out for this entertainment while you're there!: {options_list[3]}")

#This generates a random item based on the list I send through
def generate_random_item(list_of_items):
    rand_choice = random.choice(list_of_items)
    return rand_choice

#This determines whether the user is satisfied or not
def satisfaction_generator():
    user_input = input("Are you satisfied with your trip? (Y/N): ")
    if user_input == "N":
        return False
    else:
        print("Glad to help!")
        return True

#This should remove items for me that the user is now satisfied with
def remove_items_from_list(unwanted_list, unwanted_element):
    new_list = unwanted_list.remove(unwanted_element)
    return new_list

master_generator_function()






