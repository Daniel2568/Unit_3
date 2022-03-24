# Oregon Trail Game

#introduction
print()
print("Welcome to Oregon Trail!")
print()
print("*This is a game that is made up of text*")
print()
print("You are currently living in Independence, Missouri. You trying to make it to Oregon City,Oregon by December 31st and it is currently 03/01\nYou will have to travel 2,000 miles, and will be starting off with 500lbs of food, you will also start with 5 health... good luck.")

# User Customization/Info
player_name = input("What would you like your name to be?>")

import random 
#health status

health = 5
food = 500
miles_to_go = 2000
current_day = 1
currnt_month = 3


#Player choices 
print("What action would you like to perform?(You can travel, rest, hunt, status, help, quit)")

def travel():
    global miles_to_go 
    
    miles_travled = random.randint(30,60)
    print(f"You've travel {miles_travled} miles")

    miles_to_go -= miles_travled

def rest():
    pass

def hunt():
    pass

def status():
    pass

def help():
    print("Your goal is to get to Oregon City, Oregon by 12/31 just before winter starts or you die\n you can travel, rest, hunt, ask for help, check your player status, or quit\n")

def quit():
    pass

def eat():
    pass
    global food
    food -= 5 
    print(f"You've consumed 5lbs of food")

#Game loop 
while True:
    pass
    user_choice = input("")



