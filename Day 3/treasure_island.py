print(" Welcome to the Treasure Island ")

print(" Your mission is to find the treasure ")

directions = str(input(" You are at a cross road, where do you wan to go: left or right:  "))

if directions == "left":
    lake_movement = str(input(""" You come to a lake. There is an island in the middle of the lake. Type wait to "wait" for a boat. Type "swim" to swim across: """))
    if lake_movement == "wait":
        door_selection = str(input(""" You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue. WHich are you choosing:  """))
        if door_selection == "yellow":
            print(" You Win !!!!!!!!!!!!!!!!!! ")
        else:
            print(" You Lose ")
    else:
        print(" You Lose ")
else:
    print(" You Lose ")
