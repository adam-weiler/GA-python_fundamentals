#Exercise 5

#Example 1:
# while True:
#     print("I'm an infinite loop!")


# Example 2:
counter = 1

while counter < 4:
    print("counter currently at {}.".format(counter))
    counter += 1 #Increases the value of counter by 1.
#Outputs 'counter currently at 1', 'counter currently at 2', 'counter currently at 3'


# Exercise 1:
counter = 0
distance = 0

while counter < 4:
    counter += 1

    print("Would you like to walk or run?")
    speed = input().lower()

    if (speed == "walk"):
        distance += 1
    elif (speed == "run"):
        distance += 5
        
    print("Distance from home is {}km.".format(distance))
#Outputs 'Would you like to walk or run?' and 'Distance from home is {distance}km' four times.