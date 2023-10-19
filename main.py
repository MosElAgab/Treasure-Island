from ASCII import (welcome_ASCII, game_over_ASCII)
print(welcome_ASCII)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
pass_key = None
# answer = None

# stage 1
if pass_key == None:
    answer = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n').lower()

if answer == 'left':
    pass_key = True
elif answer == 'right':
    pass_key = False
    print('Fall into a hole')
    print(game_over_ASCII)
else:
    pass_key = False
    print('You chose an option that does not exist. \nGame Over')
    print(game_over_ASCII)

# stage 2
if pass_key == True:
    answer = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if answer == 'wait':
        pass_key = True
    elif answer == 'swim':
        pass_key = False
        print('Attacked by trout. Game Over.')
        print(game_over_ASCII)
    else:
        pass_key = False
        print('You chose an option that does not exist. \nGame Over')
        print(game_over_ASCII)

# final stage
if pass_key == True:
    answer = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
    if answer == 'yellow':
        print("You found the treasure! You Win!")
        print(welcome_ASCII)
    elif answer == 'blue':
        print("You enter a room of beasts. Game Over.")
        print(game_over_ASCII)
    elif answer == 'red':
        print("It's a room full of fire. Game Over.")
        print(game_over_ASCII)
    else:
        print("You chose a door that doesn't exist. Game Over.")
        print(game_over_ASCII)
