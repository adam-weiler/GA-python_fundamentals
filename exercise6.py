#Exercise 6

#Question 1:
distance = 0

while False:
    print("Would you like to walk or run?")
    user_input = input().lower()

    if user_input == "walk":
        distance += 1
    elif user_input == "run":
        distance += 5
    elif user_input == "go home":
        print("Good job! You travelled {}km.".format(distance))
        break
    else:
        print("That command does not exist.")
        
    print("Distance from home is {}km.".format(distance))
#Outputs 'Would you like to walk or run?' and 'Distance from home is {distance}km' each time the loop runs.
# Runs until user enters 'go home' and outputs 'Good job! You travelled {km}km.'
# Outputs 'That command does not exist' if the user enters anything except 'walk', 'run', or 'go home'.


#Question 2:
distance = 0
energy = 100

while True: #Runs until user inputs 'go home' or has less-than-equal-to 0 energy.
    print("Would you like to walk or run?")
    user_input = input().lower()

    if user_input == "walk": #If user inputs 'walk'. Distance increases by 1, energy increases by 10.
        distance += 1
        energy += 10
    elif user_input == "run": #If user inputs 'run'. Distance increases by 5, energy decreases by 25.
        distance += 5
        energy -= 25
    elif user_input == "go home": #If user inputs 'go home'. Provides final report on distance and energy. Breaks the loop.
        print("Good job! You travelled {}km. You have {} energy left.".format(distance, energy))
        break
    else: #Else user's command is not recognized.
        print("That command does not exist.")

    if energy <= 0: #If user has run out of energy. Breaks the loop.
        print("You have run out of energy! Distance from home is {}km.".format(distance))
        break
    else: #Else provides a report on distance and energy.
        print("Distance from home is {}km. You have {} energy".format(distance, energy))