# import random so we can use the function to pick a number from a range
import random

# variables
get_number = input("Enter a number between 1 and 100: ")
numbers_list =range(1,100)
target = random.choice(numbers_list)
my_guess = int(get_number)


#code
counter = 0
# set counter for number of maximumgueses
while counter <= 5:
# if somebody enters value above 100, throw an error, ask for another guess
    if  my_guess > 100:
        print("You're number ", my_guess, " is invalid. Please enter a number between 1 and 100")
        get_number = input("Enter a number between 1 and 100: ")
# if somebody enters value below 1, throw an error, ask for another guess
    elif my_guess < 1:
         print("You're number ", my_guess, " is invalid. Please enter a number between 1 and 100")
         get_number = input("Enter a number between 1 and 100: ")

# if the value entered is valid but not equal to selected value, ask for another guess
    elif my_guess != target:
        print("Your guess ", my_guess, " is valid but it is not equal to the number I selected")
        print('you can have another guess!')
        get_number = input("Enter a number between 1 and 100: ")

# if the value entered is equal to selected value, print out that they guessed correctly and exit the game
    else: 
        my_guess == target
        print("Your number is equal to the number I selected")
        print('you win!')
        break
# increment the counter when we pass through the loop until we hit out guess limit
    counter += 1

# if we run out of guesses, print out you lose
if counter == 6:
    print('\n You lose. You\'re out of guesses. The number I selected was ', target)

    

