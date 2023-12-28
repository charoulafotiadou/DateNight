import json

def save_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        # Handle the case where the file doesn't exist yet
        return {}

# File to store couples data
file_name = "couples_data.json"

print("Welcome to your Date Night!")
print("---------------------------")
print("Are you struggling figuring out what to do tonight? I am here to help...")

# Staging area

# Load existing couples data from file
couples_list = load_from_file(file_name)

have_played_before = input("Have you played this before? ")

if have_played_before.upper() == "YES":
    couple_name = input("What was the nickname you used? ")
    couple_name_upper = couple_name.upper()
    if couple_name_upper in couples_list:
        print("Welcome back, {}!".format(couple_name))
    else:
        print("Nickname not found in the list.")
        couple_name = input("Come up with a nickname for the both of you as a couple! ")
        couple_name_upper = couple_name.upper()
        couples_list[couple_name_upper] = {'Game_chosen': None}  # Subcategory for game choice
        print("Nickname {} added to the list.".format(couple_name))
else:
    couple_name = input("Come up with a nickname for the both of you as a couple! ")
    couple_name_upper = couple_name.upper()
    couples_list[couple_name_upper] = {'Game_chosen': None}  # Subcategory for game choice
    print("Nickname {} added to the list.".format(couple_name))

hungry = input("Are you hungry? ")

def eatout(answer):
    if answer.upper() == 'YES':
        eat_out = input("Do you want to make dinner? " )
        if eat_out.upper() == 'NO':
            order_or_go_out = input("Would you like to order or go out? ")
            if order_or_go_out.upper() == "ORDER":
                order_options()
            elif order_or_go_out.upper() == "GO OUT":
                eatout_options()
            else:
                print("Please type 'Order' or 'Go out'")
        else:
            make_dinner_option()
    else:
        other_options()

def eatout_options():
    fancy_or_casual = input("Care to dress up or just grab a bite? ")
    if fancy_or_casual.upper() == "DRESS UP":
        print("Nice choice!! Here is your date night!! Go..gooo!")
    else:
        print("Oh please dress up! It is a date night after all! Have fun!")

def order_options():
    food_type = input("What would you like to eat? ")
    if food_type.upper() == "PASTA":
        print("Sounds like Italian today...Tip Top Street is a great option!")
        print("But...why not make it fun and cook since you are staying home?")
    elif food_type.upper() == "MEAT":
        print("You have to be more specific...")
        meat = input("Let's see...there is souvlaki, gyros, burger, sausage, steak and many many more...Choose one! ")
        if len(meat) > 2:
            print("I think BOX will serve you better...bye!")
        else:
            print("Don't try to trick me! I said choose!")
            print("Oh wait...bye!")
    elif food_type.upper() == "SALAD":
        print("Think of your boyfriend...")
        order_options()
    elif food_type.upper() == "SWEET":
        print("Sweet crepe? Waffle? Lavacake? Too many options!! Can't help there..")
    else:
        print("Oh you typed something that either doesn't make sense, or I wasn't programmed to think...better luck next time!")
        order_options()

def make_dinner_option():
    print("Nice! Here are the instructions! First, figure out what you want to cook! Once ready type yes: ")
    ready = input("Are you ready? ")
    chef = input("Who is going to be the chef? ")
    sou_chef = input("Who is going to be the sous chef? ")
    print("Debug: Inputs received - Ready: {}, Chef: {}, Sous Chef: {}".format(ready, chef, sou_chef))
    
    print("Ok! Let's get started! " + chef + " I hope you have some cooking experience because you have to run this kitchen!")
    print(sou_chef + " You better listen to " + chef + "...")
    print("Debug: After chef and sous_chef statements")
    print("Now, we have to do this in a fun way...choose your aprons...and that only you should wear! Have fun ;)")

def other_options():
    activity = input("Are you feeling lazy? ")
    if activity.upper() == "YES":
        print("Maybe watch a movie? But make an atmosphere first..this has to be a date night! Light up some candles, maybe get a bottle of wine?")
    else:
        print("Well, now we are talking...Visit this website. It will help: https://www.happilyeveradventures.com/at-home-date-night-ideas/")
        
        # Initialize answer to an invalid value to enter the loop
        answer = None

        while answer is None:
            try:
                answer = int(input("Which number did you choose? "))
                if not (1 <= answer <= 25):
                    raise ValueError("The chosen number is not between 1 and 25.")
            except ValueError as e:
                print(e)
                answer = None  # Reset answer to None to repeat the loop

        couples_list[couple_name_upper]['Game_chosen'] = answer

    print(couples_list)

# Save updated couples data to file at the end of the script
save_to_file(couples_list, file_name)



eatout(hungry)
save_to_file(couples_list, file_name)

# Additional print statement
print("Thank you for using the Date Night script! Press Enter to exit.")
# Wait for user to press Enter before exiting
input()
