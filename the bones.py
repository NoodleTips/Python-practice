# def function_1():
#     while True:
#         waffles = input("Thiccer than a birthday cake? ")
#         if waffles.isdigit():
#             waffles = int(waffles)
#             if waffles > 0:
#                 break
#             else:
#                 print("I too, smoother myself in vaseline and crawl around my front lawn at 2AM like a slug. 0.o")
#         else:
#             print("Try keto. All you do is vigorously maintain a period of sweat and just glizzy gobble shmeat all day for max gainz.")
#
#         return waffles
#
# def get_number_of_lines():
#     while True:
#         lines = input("Enter the number of lines to bet on")
#         if lines.isdigit():
#             lines = int(lines)
#             if 1 <= lines <= MAX_LINES:
#                 break
#             else:
#                 print("Enter a valid number of lines.")
#         else:
#             print ("Please enter a number.")
#     return lines
#
#
# def main():  #! <---------------
#     balance = function_1()            # Start thinking of something or someone. A book, waffle-iron, your cat,
#     a group of cats,
#                                       # a type of cat, etc...
#     lines = get_number_of_lines()     # Once you think of something or a goal.
#                                       # Think about the features, the individual parts, the next sub-level down from
#                                       # the goal. Stick these parts under main()
#     print(balance, lines)
#
#     main()

#############################################################################
#############################################################################

# a = b = c = 8
#or#
# a, b, c = 1, 2, 3
# print(b)
'''You can initialize multiple variables with the same value...'''
#-------------------
# user = input("Hello, what is your name?: ")
# print("Welcome", user)
#
# languages = input("What languages do you know/speak?: ")
# print("That's cool that you know",languages,end = "!\n")

'''input() allows you to get info from the user, usually in the form of a question. The info is stored in the 
variable and later called.'''
#-------------------

# x = 3
#
# if x % 2 != 0: # If(true), do this
#     print('The number is an ODD number.')
# else: # Otherwise, do this.
#     print('The number is an EVEN number.')
#
'''If/else statements take a variable and gives it possible options depending on if its true or not.'''
#-------------------

# a = input("Please, enter a number: ")
# b = input("Please enter another number: ")

# sum = a + b                           # Output: Total/Data Type: [ 3211 ]/ <class 'str'>
# sum = int(a) + int(b)                 # Output: Total/Data Type: [ 43 ]/ <class 'int'>
# sum = float(sum)                      # Output: Total/Data Type: [ 43.0 ]/ <class 'float'>
# sum = chr(int(sum))                   # Output: Total/Data Type: [ + ]/ <class 'str'>
# print('\nTotal/Data Type:' ,'[',sum,']/', type(sum))

'''This is called "Casting data types". You can change the format of your output.'''
#-------------------

# quarter = ['January','February','March']
# coords = [[1,2,3],[4,5,6]]

# print('First month:',quarter[0])
# print('Second month:',quarter[1])
# print('Third month:',quarter[2])

# print('\nTop Left 0,0 :', coords[0][0])
# print('\nBottom Right 1,2 :', coords[1][2])
#
# print('\nSecond Month First Letter:', quarter[1][0])

# coords:
#    (0) (1) (2)
# (0)[1] [2] [3]
# (1)[4] [5] [6]

'''This is how you write and index lists.'''
#-------------------

# basket = ['Apple','Bun','Cola']
# crate = ['Egg','Fig','Grape']
# deleted_items = []

# print('Basket list: ',basket)
# print('Basket Elements:',len(basket))
#
# basket.append('"Damson"')
# print('Appended:',basket[-1])                              #Output: Appended: "Damson"
# print('Last item removed:',basket.pop())                   #Output: Last item removed: "Damson"
# print('Basket list:',basket)                               #Output: Basket list: ['Apple', 'Bun', 'Cola']

# basket.extend(crate)
# print('Extended:', basket)                                  # Output: Extended: ['Apple', 'Bun', 'Cola', 'Egg', 'Fig', 'Grape']
# deleted_items.append(basket.pop())                          # Appends to "deleted_items" from a pop in basket
# print("Last deleted: "+ str(deleted_items[-1]))             # Last deleted: Grape
# print('Item removed. Current basket:',basket)               # Output: Item removed. Current basket: ['Apple', 'Bun', 'Cola', 'Egg', 'Fig']
# del basket[1:3]
# print('Slice removed:', basket)                             # Output: Slice removed: ['Apple', 'Egg', 'Fig']

'''This is how you manipulate lists. You can remove them or append them. Pop them or slice 'em. You can pop an item 
off one list and append it to another and use negative indexing to reference the last item removed.'''
#-------------------

# zoo = ('kangaroo','Leopard','Moose')    # Tuple
# bag = {'Red','Green','Blue'}            # Set
# box = {'Red','Purple','Yellow'}         # set
#
# print('Tuple:', zoo,'\nLength:', len(zoo))                  # Tuple: ('kangaroo', 'Leopard', 'Moose')
#                                                             # Length: 3
# print('Type:',type(zoo))                                    # Type: <class 'tuple'>
#
#
#
# bag.add('Yellow')                                           # Adds 'yellow' to the tuple
# print("\nSet:",bag,"\nLength:",len(bag))                    # Set: {'Red', 'Yellow', 'Green', 'Blue'}
#                                                             # Length: 4
# print("Type:",type(bag))                                    # Type: <class 'set'>
#
# print("\nIs Green in bag set?:",'green' in bag)             #Is Green in bag set?: False
# print("Is Orange in bag set?:",'orange' in bag)             #Is Orange in bag set?: False
#
# print('\nSet:',box,'\nLength:',len(box))                    # Set: {'Yellow', 'Red', 'Purple'}
#                                                             # Length: 3
# print('Common to both sets:',bag.intersection(box))         # Common to both sets: {'Red', 'Yellow'}

'''This are restricting lists. Tuples are immutable and sets are not, but can be using 'frozenset()'.'''
#-------------------

# userSys = {'Name':'Bob','System':'Windows'}
# userLang = {'Name':'Bob','Language':'Python'}
# dict = userSys | userLang

# print('\nDictionary:',dict)                                 # Dictionary: {'Name': 'Bob', 'System': 'Windows', 'Language': 'Python'}
# print("\nLanguage:",dict["Language"])                       # Language: Python
# print("\nKeys:",dict.keys())                                # Keys: dict_keys(['Name', 'System', 'Language'])

# del dict['Name']                                            # Deletes 'Name' from dict
# dict['user'] = 'Mitchell'                                   # Changes the name of the user
# print('\nDictionary:',dict)                                 # Dictionary: {'System': 'Windows', 'Language': 'Python', 'user': 'Mitchell'}
#
# print("\nIs there a 'Name' key?:",'Name' in dict)           # Is there a 'Name' key?: False

'''This is how you associate list elements and can even merge them into a dictionary with key/value pairs.'''
#-------------------

# cmd = input('Enter STOP or GO:').upper()                    # Input prompt for match case
# num = int(input('Guess the number:'))                       # Input prompt for if/else statement
# secret = 45
#
# if num < 45:
#     print(f'The secret number is higher than {num}!')
# elif num > 45:
#     print(f'The secret number is lower than {num}!')
# else:
#     print(f'The secret number was: {secret}! Congrats!')

# if num > 5:
#     print('Number exceeds 5\n')
# elif num < 5:
#     print('Number is less than 5\n')
# else:
#     print('The number is 5\n')

# match cmd:                            # Python 3.9 doesn't support match case :( wack.
#     case 'GO':
#         print('Starting...')
#     case 'STOP':
#         print('Stopping...')
#-------------------

# i = 1
# while i < 4:
#     print('\nOuter Loop Iteration:,', i)
#     i += 1
#     j = i
#     while j < 5:
#         print('\tInner Loop Iteration:', j)
#         j += 1
                                        # Outer Loop Iteration:, 1
                                        # 	Inner Loop Iteration: 2
                                        # 	Inner Loop Iteration: 3
                                        # 	Inner Loop Iteration: 4
                                        #
                                        # Outer Loop Iteration:, 2
                                        # 	Inner Loop Iteration: 3
                                        # 	Inner Loop Iteration: 4
                                        #
                                        # Outer Loop Iteration:, 3
                                        # 	Inner Loop Iteration: 4

''' 'While True' allows continuous iteration through both loops while the statement 
remains true with i+=1 (i = i + 1)'''
#-------------------

# chars = ['A','B','C']
# fruit = ('Apple','Banana','Cherry')
# dict = {'name':'Mike','ref':'Python','sys':'Windows'}

# print('\nElements:\t', end = '')
# for item in chars:
#     print(item, end = '')             # Elements:	ABC

# print('\nEnumerated:\t', end = '')
# for item in enumerate(chars):
#     print(item, end = '')             # Enumerated:	(0, 'A')(1, 'B')(2, 'C')

# print('\nZipped:\t', end = '')
# for item in zip(chars, fruit, strict=True):
#     print(item, end = '')

# print('\nPaired:')
# for key, value in dict.items():
#     print(key, '=', value)            # Paired:
                                        # name = Mike
                                        # ref = Python
                                        # sys = Windows
'''These are various ways to loop over an item(s). It is like
 'While True' but it has a determined start and end.'''
#-------------------

# for i in range(1,4):
#     for j in range(1,4):
#         print('Running i=', i, 'j =',j)

# Running i= 1 j = 1
# Running i= 1 j = 2
# Running i= 1 j = 3
# Running i= 2 j = 1
# Running i= 2 j = 2
# Running i= 2 j = 3
# Running i= 3 j = 1
# Running i= 3 j = 2
# Running i= 3 j = 3

# for i in range(1,4):
#     for j in range(1,4):
#         if i == 2 and j == 1:
#             print('Breaks inner loop at i = 2 j = 1')
#             print('Running i =', i, 'j =', j)
#             break

# for i in range(1,4):
#     for j in range(1,4):
#         if i == 1 and j == 1:
#             print('Continues inner loop at i = 2 j = 1')
#             continue

''' 'Break' and 'continue' allows you to end it 
or continue on to the next piece of code.'''
#-------------------

# global_var = 1      # global variable
#
# def my_vars():      # custom function
#     local_var = 2   # local variable
#     global inner_var#
#     inner_var = 3
#     print('Coerced Variable:', inner_var)
#     print('Local Variable:', local_var)
#     print('Global Variable:', global_var)

# my_vars()           # call the custom function

# Coerced Variable: 3
# Local Variable: 2
# Global Variable: 1
''' When it comes to scope, global are variables that are made outside of functions and can be referenced anywhere.
 Local scope are variables made inside the function and can be referenced outside of that function, unless you state 
 'global' before it.'''
#-------------------

# def echo(user, lang, sys):
#     print('User:',user,'\nLanguage:',lang,'\nPlatform:',sys)

# echo('Mike','Python','Windows')

# User: Mike
# Language: Python
# Platform: Windows

# echo(lang = 'Python',sys = 'Mac OS',user = 'Anne')

# User: Anne
# Language: Python
# Platform: Mac OS

# def mirror(user = 'Carole', lang = 'Python'):
#     print("\nUser:", user,"\nLanguage:",lang)
#
# mirror()

# User: Carole
# Language: Python

# mirror(lang = 'Java')
# mirror(user = 'Tony')
# mirror('Susan', 'C++')

# User: Carole
# Language: Python
#
# User: Carole
# Language: Java
#
# User: Tony
# Language: Python
#
# User: Susan
# Language: C++

''' You can change/update the properties of items when you supply a(n) argument(s) to a custom function. '''
#-------------------

# num = input('Enter an integer:')
#
# def square(num):
#     if num.isdigit():                   # Verifies if the input is a digit and then turns into an integer and then
#         num = int(num)                  # multiplies itself with itself to get squared.
#         return num * num
#     else:
#         return 'Invalid Entry'
#
# print(num,'Squared Is:',square(num))    #16 Squared Is: 256


# def square(num):
#     if num.isdigit():
#         num = int(num)
#         return num * num
#     else:
#         return None
#
# result = None
# while result is None:
#     num = input('Enter a number:')
#     result = square(num)
#     if result is None:
#         print('Invalid Entry. Please enter a valid number.')
#
# print(num,'Squared Is:', result)

# This version will keep asking for a valid integer until a valid one is inputted. The 'square' function returns
# 'None' if the input not a valid integer. A while loop is used to keep asking for input.

# Invalid Entry. Please enter a valid number.
# Enter a number:beans
# Invalid Entry. Please enter a valid number.
# Enter a number:8
# 8 Squared Is: 64

''' You can filter certain data types for when asking for input.'''
#-------------------

# def function_1(x)  :return x ** 2
# def function_2(x): return x ** 3
# def function_3(x): return x ** 4

# callbacks = [function_1,function_2,function_3]
#
# print('\nNamed Functions:')
# for function in callbacks: print('Result:',function(3))

# Named Functions:
# Result: 9
# Result: 27
# Result: 81

# callbacks = \
# [lambda x:x**2,lambda x:x**3,lambda x:x**4]
# print('\nAnonymous Functions:')
# for function in callbacks:print('Result:', function(3))

# Named Functions:
# Result: 9
# Result: 27
# Result: 81
#
# Anonymous Functions:
# Result: 9
# Result: 27
# Result: 81

'''The lambda function can be used to make small one-liner functions. You can also use lambda to like sort things. 
The expression would be something like 'sorted_numbers = sorted(numbers, key=lambda x: -x)'.
sorted_numbers would use the sorted() function and pass a list named 'numbers' with a lambda key of 'x' being 
negatively indexed to sort in descending order. '''

#-------------------

# title = '\nThis shit is easy\n'
#
# for char in title:
#     print(char, end = '')
#
# for char in title:
#     if char == 'y':
#         print('*', end = '')
#         continue
#     print(char, end = '')
#
# for char in title:
#     if char == 'y':
#         print('*', end = '')
#         pass
#     print(char, end = '')


# This shit is easy
#
# This shit is eas*
#
# This shit is eas*y

''' The "end = '' " replaces the default newline character (\n) with a space. So instead of moving to the next line 
to print, the cursor will add a space and print the next line on the same line.

-The 'pass' keyword basically is a no-operation statement that does nothing but is used as a placeholder for future 
changes but is needed to circumvent syntax errors. 

-The 'continue' keyword is used inside a loop to skip the remaining part of the loop body. 
The program jumps back to the start of the loop and continues onto the next iteration.'''
#-------------------
# def fibonacci_generator():
#     a = b = 1
#     while True:
#         yield a
#         a, b = b, a+b
#
# fib = fibonacci_generator()
# for i in fib:
#     if i > 100:
#         break
#     else:
#         print('Generated:',i)

''' The fibonacci_generator function  init's and sets a and b to 1 then yields a and reads b = a+b and repeats. The 
for loop cycles while the generator tally is under 100 and then prints it.'''
#-------------------

# title = 'I have the hershey squirts'
# try:
#     print(titel)
# except NameError as msg:
#     print(msg)

# name 'titel' is not defined

# This prevents the program from crashing due to a NameError but instead catches the exception and assigns it to the
# variable 'msg' and prints that instead.

# except(NameError, IndexError, ValueError) as msg:
# print(msg)

# you can circumvent a crash by including multiple exception types with a list:

# day = 33
# try:
#     if day > 31:
#         raise ValueError('Invalid Day Number')
# except ValueError as msg:
#     print('The Program found An',msg)
# finally:
#     print('But Today Is Beautiful Anyway.')

# The Program found An Invalid Day Number
# But Today Is Beautiful Anyway.

''' This defines the variable as 33. The 'try' block checks whether the value of 'day' is greater than 31. If it is, 
the 'raise' statement raises a 'ValueError' exception with the message. The except block catches the 'ValueError 
exception and assigns it to the variable 'msg'. This allows you to have distinct messages for each type of error and 
than eventually gets added onto the print. The finally block executes the print function regardless if an exception 
occurred or not. '''
#-------------------









