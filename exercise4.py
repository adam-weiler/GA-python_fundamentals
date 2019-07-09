#Exercise 4

#Question 1:
print("Please enter a number:")
number = int(input())

if (number >= 100):
    print("That's a big number!")
else:
    print("Why not dream a little bigger?")
#Outputs either 'That's a big number!' or 'Why not dream a little bigger?'


#Question 2
print("Please enter your age:")
age = int(input())

if (age > 105):
    print("I'm not sure I believe you.")
else:
    if (age > 32):
        print("You are {} years older than me.".format(age - 32))
    else:
        print("You are {} years younger than me.".format(32 - age))
#Outputs either 'I'm not sure I believe you', or 'You are {age} years older than me', or 'You are {age} years younger than me'.


#Question 3
my_name = "Adam"
print("What is your name?")
user_name = input().capitalize()

if my_name == user_name:
    print("We have the same name!")
else:
    print("We have different names!")
#Outputs either 'We have the same name!', or 'We have different names!'


#Question 4
secret_number = 42
print("Please enter a number:")
user_num = int(input())

if user_num == secret_number:
    print("You win!")
elif abs(user_num - secret_number) == 1:
    print("So close!") 
else:
    print("Try again.")
#Outputs either 'You win!', or 'So close!', or 'Try again.'