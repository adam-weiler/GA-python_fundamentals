#Exercise 3

#Example 1
print("What is your name?")
user_name = input()
print("Hello, {}.".format(user_name))
#Outputs 'Hello, {user_name}.'


#Example 2
secret_password = "please"
print("What's the password?")
password_attempt = input()

correct_or_not = (password_attempt == secret_password)

print("That's {}!".format(correct_or_not))
#Outputs 'That's {correct_or_not}!'


#Example 3
print("How many cookies have been eaten?")
eaten = int(input())

#Converts eaten (the user input) to integer and subtract it from 12.
remaining_cookies = 12 - eaten

print("There are {} cookies left.".format(remaining_cookies))


# Example 4
print("How old are you?")
user_age = int(input())

print("You were probaly born in {}.".format(2019 - user_age))


#Example 5A
my_number = 5

if my_number < 4:
    print("Hello")
print("Bonjour")

if my_number > 4:
    print("Hi there")
print("How are you?")
#Ouputs either "Hello", "Bonjour", "How are you?"...
#Or outputs "Bonjour", "Hi there", "How are you?"


#Example 5B
print("Please print a number:")
your_number = int(input())

if your_number > 5:
    print("This line will run if the user enters a number greater than 5.")

print("This line always runs.")
#Outputs either 'This will will run...' and 'This line always runs.'...
#or outputs 'This line always runs.'


#Example 6
print("Enter a number:")
number = int(input())

if int(number > 0):
    print("{} is positive.".format(number))
else:
    print("{} is negative.".format(number))
#Ouputs either '{number} is positive.' or '{number} is negative.'


#Example 7
print("Add values for x and y:")
x = int(input())
y = int(input())

if x > y:
    print("x is greater than y!")
elif x < y:
    print("x is less than y!")
else:
    print("x equals y!")
#Outputs either 'x is greater than y!', 'x is less than y!', or 'x equals y!'