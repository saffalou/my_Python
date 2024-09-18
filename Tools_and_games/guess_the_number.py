import random


get_number = input("Enter a number between 1 and 100: ")
numbers_list =range(1,100)
target = random.choice(numbers_list)
my_guess = int(get_number)



counter = 0

while counter <= 5:

    if  my_guess > 100:
        print("You're number ", my_guess, " is invalid. Please enter a number between 1 and 100")
        get_number = input("Enter a number between 1 and 100: ")
    elif my_guess < 1:
         print("You're number ", my_guess, " is invalid. Please enter a number between 1 and 100")
         get_number = input("Enter a number between 1 and 100: ")
    elif my_guess != target:
        print("Your guess ", my_guess, " is valid but it is not equal to the number I selected")
        print('you can have another guess!')
        get_number = input("Enter a number between 1 and 100: ")
    else: 
        my_guess == target
        print("Your number is equal to the number I selected")
        print('you win!')
        break

    counter += 1

if counter == 6:
    print('\n You lose. You\'re out of guesses. The number I selected was ', target)

    

