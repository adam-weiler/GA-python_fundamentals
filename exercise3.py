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