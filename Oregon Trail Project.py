# Oregon Trail Game

import random

#introduction
print()
print("Welcome to Oregon Trail!")
print()
print("*This is a game that is made up of text*")
print()
print("You are currently living in Independence, Missouri. You trying to make it to Oregon City,Oregon by December 31st and it is currently 03/01\nYou will have to travel 2,000 miles, and will be starting off with 500lbs of food, you will also start with 5 health... good luck.")

# User Customization/Info
player_name = input("What would you like your name to be?>")

#global variables
MONTHS = ['dumby', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
MONTHS_WITH_30_DAYS = ['April', 'June', 'September', 'November']
health = 5
food = 500
miles_to_go = 2000
current_day = 1
current_month = 3


#Player Functions



def travel():
    global miles_to_go, current_day
    
    days_this_travel = random.randint(3,7)
    miles_traveled  = random.randint(30,60)

    print(f"You have traveled {miles_traveled} miles")
    current_day += days_this_travel

    miles_to_go = miles_traveled

    add_day(days_this_travel)
    consume_food(days_this_travel)

def add_day(days):
    global current_day, current_month
    current_day += days 


# Month rule
    if MONTHS[current_month] in MONTHS_WITH_30_DAYS:
        if current_day > 30:
            current_day -= 30
            current_month += 1
    
    else:
        if current_day > 31:
            current_day -= 31
            current_month += 1

    consume_food(days)

def consume_food(days):
    global consumed_food

    consumed_food = 5 * days
    
     


def status():
    print()
    print(f"You have {miles_to_go} miles to go")
    print()
    print(f"It is {MONTHS[current_month]} {current_day}.")
    print()
    print(f"You have {health} remaining health")
    print()
    print(f"You have {food} remaining food")

def rest():
    global health
    days_this_rest = random.randint(2,5)
    print(f"You rested for {days_this_rest} days")
    health += 1
    if health >= 5:
        print("You probably shouldnt rest if your health is full\nYou cant have more than 5 health")
        health -= 1

    add_day(days_this_rest)
    consume_food(days_this_rest)

def hunt():
    global food

    days_this_hunt = random.randint(2,5)
    food += 100

    add_day(days_this_hunt)




def help():
    print()
    print("Your goal is to get to Oregon City, Oregon by 12/31 just before winter starts or you die\nRemember you can travel, rest, hunt, ask for help or type 'help', check your player status, or quit")

def quit():
    global game_over
    print()
    print("Hope you enjoyed the game up to this point, have a nice day")
    game_over = True 

#Game loop 
game_over = False
reset = False 

while not game_over:
    user_choice = input("What action would you like to perform?>")

    if user_choice == 'travel':
        travel()
    if user_choice == 'status':
        status()
    if user_choice == 'rest':
        rest()
    elif user_choice == 'hunt':
        hunt()
    elif user_choice == 'quit':
        quit()
    elif user_choice == 'help':
        help()
    else: 
        print("Im not sure I understood your action choice")

while game_over == True:
    if miles_to_go == 0 and current_month <= 12 and current_day <= 30:
        print("Good job you made it!")
        print()
        print("Hope you enjoyed the game and hope you have a great day")
    elif health == 0 or food == 0 or miles_to_go > 0 and current_day == 31 and current_month == 12:
        print("It seems you have died to either starvation, animal, or you didn't make it in time\nYou can type 'play again' if you wish to play again or 'quit' if you wish to stop playing")
    if user_choice == 'play again':
        reset = True 
    elif user_choice == 'quit':
        quit()




