print("Welcome to your Date Night!")
print("---------------------------")
print("Are you struggling figuring out what to do tonight? I am here to help...")

# Staging area

q1 = input("Are you hungry? ")
q1_capitals = q1.upper()

def make_dinner_option():
    # Define your make_dinner_option logic here
    pass

def eatout(answer):
    if answer == 'YES':
        q1_a = input("Do you want to eat out? " )
        q1_a_capitals = q1_a.upper()
        if q1_a_capitals == 'YES':
            q1_a_1 = input("Would you like to order or go out? ")
            q1_a_1_capitals = q1_a_1.upper()
            if q1_a_1_capitals == "ORDER":
                order_options(q1_a_1_capitals)
            elif q1_a_1_capitals == "GO OUT":
                eatout_options(q1_a_capitals)
            else:
                print("Please type 'Order' or 'Go out'")
        else:
            make_dinner_option()

def eatout_options(answer):
    q1_a_1 = input("What would you like to eat? " )
    q1_a_1_capitals = q1_a_1.upper()
    if q1_a_1_capitals == "PASTA":
        print("I have some options for you...")
        print("You")
    elif q1_a_1_capitals == "MEAT":
        print("Why not ...")
    else:
        print("Give it some more thought...")

eatout(q1_capitals)
