# import datetime
# import random
# import asyncio


# Python Journal #

# ! 1
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

# today = datetime.date.today()
# current_year = today.year
#
#
# user_name = input('Enter your name: ')
# user_age = int(input('Enter your age in years: '))
#
# remaining_years = 100 - user_age
# hundredth_year = current_year + remaining_years
# print("You will turn one hundred on the year: ", hundredth_year)
# ''' user_name asks for the name and user_age asks for the age. remaining_years subtracts the age from 100.
# hundredth_year adds remaining years to current_year which is pulled from today.year method from imported datetime.'''
# *###########################################################
# ! 2
# Ask the user for a number.
# Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?


# random_number = int(input('Tell me a random number: '))
# if (random_number % 2) == 0:
#     print('The number is even.')
# else:
#     print('The number is odd.')
# ''' random_number is an input integer with a string asking for a random number. if random_number mod 2 = 0,
# then it is even and print 1st statement, else print 2nd statement if the number is odd.'''
# *###########################################################
# ! 3
# from operator import index
# Take a list, say for example this one:
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# b = []
#
# for x in a:
#     if x < 5:
#         b.append(x)
#         print(b)
# ''' for the item in a, if the item is less than 5, append it to b and then print it.'''
# *###########################################################
# ! 4
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

# user_number = int(input("Give me a random number: "))
# results = "The divisors include: "
# print(results)
# for i in range(1, user_number+1):
#     if (user_number % i == 0):
#         print(i)
# ''' user_number is an input integer asking for a random number. results is a string as a title for the results to
# follow. for item in range from 1 to the users number with +1 cadence, if the users number is mod whatever the item
# is and it equals 0, print the items.'''
# *###########################################################
# ! 5
# Take two lists, say for example these two:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without
# duplicates). Make sure your program works on two lists of different sizes.


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# '''need to print a list from a set. The x for x in list a, if x also in b. it should print like values from the two
# lists.'''

# print(list(set(x for x in a if x in b)))

# *###########################################################
# ! 6
# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that
# reads the same forwards and backwards.)

# user_string = input("Enter a word to check: ")
#
#
# while len(user_string) > 2:
#     if user_string.lower() == user_string[::-1].lower():
#         print("{} is a palindrome".format(user_string))
#         break
#     else:
#         print("{} is not a palindrome".format(user_string))
#         break
# else:
#     print("The word needs to be at least 2 characters.")

# ''' while the user input string is greater than 2 characters and if the user string equals the user input string in
# reverse( [::-1] ), print the first statement. Else print second statement. If the user input string is not greater
# than 2 characters, print 3rd statement.'''

# *###########################################################
# ! 7
# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# b = []
#
# for item in a:
#     if item % 2 == 0:
#         b.append(item)
#         print(b)

# ''' for item in list "a", if the item mod 2 equals 0, then it is even and appends the item to the empty list "b" and
# prints it.'''
# *###########################################################
# ! 8
# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Do you want to play?
# Compare rock paper and scissor objects
# print out a message of the outcome
# print input new game


# options = ['Rock','Paper','Scissors']
# status = True
# while status:
#     player_1 = input("***PLAYER 1 *** \n Please choose: \n Rock \n Paper \n Scissors \n------> YOUR "
#                      "CHOICE:").lower()
#     player_2 = input("***PLAYER 2 *** \n Please choose: \n Rock \n Paper \n Scissors \n------> YOUR "
#                      "CHOICE:").lower()
#     if player_1 == player_2:
#         print("Tie")
#     elif player_1 == options[0] and player_2 == options[1]:
#         print("Player 2 won.")
#     elif player_1 == options[2] and player_2 == options[0]:
#         print("player 2 won.")
#     elif player_1 == options[1] and player_2 == options[2]:
#         print("Player 2 won")
#     else:
#         print("Player 1 won.")
#         check = input("Want to play again?").lower()
#         if check == 'no':
#             status = False
#         elif check == "yes": continue
#         else: print("Invalid input type: 'yes' or 'no'")

# '''Three options, two players. ask for input with provided string options. Then if statement with conditions that
# print strings when true.'''
# Option # 2(unfinished):
#
# def wanna_play():
#     while True:
#         player_play = input("Do you want to play a game of 'Rock, Paper, Scissors?"''  ''"y/n?: ",)
#         if player_play == 'y' or 'Y':
#             break
#         else:
#             print('oke :( ')
#     return player_play
#
# def decision():
#     while True:
#         choice = input("Please choose: \n R = Rock \n P = Paper \n S = Scissors \n------> YOUR CHOICE:")
#         if choice == "R" or "r" or "P" or "p" or "S" or "s":
#             player_choice = choice
#             print(f"You chose {player_choice}")
#             #send player_choice to global
#             break
#         else:
#             print("Please enter a valid choice.")
#     return player_choice
#                                     # print the choice
# async def op_dialogue():
#     print("OPPONENT : ...ROCK!")
#     await asyncio.sleep(1)
#     print("...")
#     await asyncio.sleep(1)
#     print("OPPONENT : ...PAPER!")
#     await asyncio.sleep(1)
#     print("...")
#     await asyncio.sleep(1)
#     print("OPPONENT : ...SCISSORS!")
#     await asyncio.sleep(1)
#
# def lets_play():
#     while True:
#         op_choices = ["R","r","P","p","S","s"]
#         op_choice = random.choice(op_choices)
#         if op_choice == "P" or "p" and pd = :
#             global opd = 2
#             print("*SCISSORS*")
#         elif op_choice == op_choice[1]:
#             print("*PAPER*")
#         else: print("*ROCK*")
#
# def outcome():
#     while True:
#         da_options = ['ROCK_a','PAPER_b','SCISSORS_c']
#         rbs
#         sbp
#         pbr
#         if # compare opponent choice with player choice
#     # print outcome
#
#
#
#
# def main():
#     start = wanna_play()
#     stage_1 = decision()
#     stage_2 = op_dialogue()
#     stage_3 = lets_play()
#
#
# main()

# *###########################################################
# ! 9

# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the
# number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# secret_number = random.randint(1,9)
#
# attempts = 0
# # loop for the user to guess the correct number
# while True:
#     user_guess = int(input("Guess a number between 1 and 9:"))
#     attempts += 1
#     if user_guess == secret_number:
#         print(f"Congrats, you guessed correctly in {attempts} attempts.")
#         break
#     elif user_guess < secret_number:
#         print("You guessed low.")
#     else:
#         print("You guessed high.")

# ''' I imported random mod and created the secret number. I then init 'attempts'. Then I used a loop to keep asking
# for user input guess for number. If-statement for feedback and if user guessed high, low or correct while
# incrementing
# attempts.'''
# *###########################################################
# ! 10

# Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = set(a).intersection(b)
#
# print(c)

# ''' By making 'a' a set, you automatically remove duplicates. Besides, sets support the intersection method. So
# basically this converts 'a' to a set and then performs the intersection with 'b'
# which is a list but because its part of an intersection it is also automatically converted to a set.'''
# *###########################################################
# ! 11

# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).

# def prime_guess(x):
#     if x <= 1:
#         return False
#
#     for i in range(2, int(x**0.5) + 1):
#         if x % i == 0:
#             return False
#
#     return True
#
# x = int(input("Give me a random number: "))
# def main():
#     if prime_guess(x):
#         print(f"{x} IS a prime number!")
#     else:
#         print(f"{x} IS NOT a prime number!")
#
# main()

# ''' The function "prime_guess" takes x-the users input as an argument and if the number is less than or equal to 1,
# it isn't prime and returns false. If x is greater, then it looks for divisors within its range (i). If x is divisible by i then it is not prime and returns false.
#  If x isn't divisible, its a prime number and returns True. Outputs a string with the result and the number given
#  under main().'''
# *###########################################################
# ! 12

# Write a program that takes a list of numbers
# (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.

# a = [5, 10, 15, 20, 25]
# b = []
#
# def new_list(a,b):
#     list_length = len(a)
#     b.append(a[0])
#     b.append(a[list_length -1])
#     print(b)
#
# new_list(a,b)

# [5, 25]

# '''
# Two lists, one is empty. defined "new_list" function. "list_length" var set to the length of list a. The function
# appends index 0 of a to list b as well as the negative index of list a and then prints it. Called function.
# '''


# *###########################################################
# ! 13

# Write a program that asks the user how many Fibonacci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonacci sequence is a sequence of numbers where the next number in the sequence is the sum of the
# previous two numbers in the sequence.
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

# def fib_gen(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#
#
# num = int(input('How many u want, cuh?:'))
# fib = fib_gen(num)
# print(list(fib))

# How many u want, cuh?:8
# [0, 1, 1, 2, 3, 5, 8, 13]

"""
The fib_gen() function produces the first 'n' amount of numbers in the fibonacci sequence.
I set 'a' and 'b' to 0 and 1, respectively.
For '_' in the range of 'n', yield a. I ask how many and set it to num.
I make an instance of fib_gen and name it fib and pass num to it.
I then print a list of fib.
"""
# *###########################################################
# ! 14























