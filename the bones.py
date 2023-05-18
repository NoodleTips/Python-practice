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

# chars = ['A','B','C','D','E','F']
# element = 4
# element = element/2
# def display(element):
#     assert type(element) is int, "Argument is an integer!"
#     print(f'Element {element} is {chars[element]}')
#     # print('List element', element,'=',chars[element])
#
# display(element)

''' The "assert" keyword allows you to test an expression in a True/False scenario to see if it works and can output 
a custom error message when the expression is "false". If the expression is "True", the assert keyword basically 
does nothing and the script continues. Assert keywords are removed before official releases while "except" keywords 
remain to handle runtime errors.'''
#-------------------

# def hiss(noodle = 'A Ball Python')
#     print(noodle,'says hi :D')
#
# def stare(noodle = 'A Ball Python'):
#     print(noodle,'has a blank stare OwO')
#
# def cinnamon_bun_mode(noodle = 'A Ball Python'):
#     print(noodle,'curls up to nap')

''' These are custom functions for a module for my pet Ball Python named 'noodle'.
You save the file as 'noodle.py' and import it on your project as "import noodle". '''

# import noodle

''' 
Then call the functions:

noodle.hiss()
noodle.stare()
noodle.cinnamon_bun_mode()

the output will look something like:

'A Ball Python says hi :D'
'A Ball Python has a blank stare OwO'
'A Ball Python curls up to nap'

when you pass an arg to 'Noodle' to 'noodle.hiss()'  ---> noodle.hiss('Noodle')
the output will be:

'Noodle says hi :D'
'''
#-------------------

# import sys, keyword
#
# print('Python Version:',sys.version)
# print('Python Interpreter Location:',sys.executable)
# print('Python Module Search Path:')
# for dir in sys.path:
#     print(dir)
#
# print('Python Keywords:')
# for word in keyword.kwlist:
#     print(word)

''' You can obtain information about the python interpreter and your system by importing the 'sys' and 'keyword' 
module. You can get the python version, the location of the interpreter as well as a list of built in keywords and 
can be tested using the 'iskeyword()' method. '''
#-------------------

# import math, random
#
# x = float(input('Enter a number: '))
# y = random.sample(range(1,100),6)   # a random list of 6 unique numbers between 1-100
#
#
# print('Rounded up:', math.ceil(x))
# print('Rounded down:', math.floor(x))
#
# print(x, 'Squared is:', math.pow(x, 2))
# print('The square root of', x, 'is:', math.sqrt(x))
#
# print('Your lucky numbers are:', y)

# Rounded up: 7
# Rounded down: 7
# 7.0 Squared is: 49.0
# The square root of 7.0 is: 2.6457513110645907
# Your lucky numbers are: [86, 14, 76, 38, 90, 8]

''' The 'Math' module allows the user to perform calculations. The 'random' module can be used to randomly choose 
and the 'sample()' method doesnt replace the values but simply creates a copy sample.'''
#-------------------

# from decimal import *

# item = 0.70
# rate = 1.05

# tax = item * rate
# total = item + tax

# print('Item:\t','%.2f' % item)
# print('Item:',"{:.2f}".format(item),'\n')
#
# print('Tax:\t','%.2f' % tax)
# print('Tax:',"{:.2f}".format(tax),'\n')
#
# print('Total:\t','%.2f' % total)
# print('Total:',"{:.2f}".format(total))

# Item:	 0.70
# Item: 0.70
#
# Tax:	 0.73
# Tax: 0.73
#
# Total:	 1.44
# Total: 1.44

''' 
There are two ways to format a floating point number with 2 decimal places. The first one is the old 
"printf-style" ---> "%.2f"
and the newer "str.format()" style ---> "{:.2f}".format():
'''

# print('Item:\t','%.20f' % item)
# print('Item:',"{:.20f}".format(item),'\n')
#
# print('Tax:\t','%.20f' % tax)
# print('Tax:',"{:.20f}".format(tax),'\n')
#
# print('Total:\t','%.20f' % total)
# print('Total:',"{:.20f}".format(total))

'''
Now with 20 decimal spaces. Results for rounding can be different depending on decimal spaces.
'''

# Item:	 0.69999999999999995559
# Item: 0.69999999999999995559
#
# Tax:	 0.73499999999999998668
# Tax: 0.73499999999999998668
#
# Total:	 1.43500000000000005329
# Total: 1.43500000000000005329

''' You can also use 'decimal' module and do Decimal() instead.'''
#-------------------

# from datetime import *
#
# today = datetime.today()
# print('Today is:',today)
#
# for attr in \
#     ['year','month','day','hour','minute','second','microsecond']:
#     # print(attr,':\t',getattr(today,attr))
#     print('Time',today.hour,':',today.minute,sep = '')
#
# day = today.strftime('%A')
# month = today.strftime('%B')
#
# print('Date:', day,month,today.day)

''' These are various ways to get the date and time through the datetime module.'''
#-------------------

# from time import *
#
# start_timer = time()
# struct = localtime(start_timer)
# print('\nStarting Countdown At:', strftime('%X', struct))
# i = 10
# while i > -1:
#     print(i)
#     i -= 1
#     sleep(1)
#
# end_timer = time()
# difference = round(end_timer - start_timer)
#
# print('\nRuntime:',difference,'Seconds')

'''
Import time() function and pass it thru localtime() and print the countdown start time. set i to 10. while i is 
greater than -1, print i and reset i with a -1 cadence then sleep for 1 second. Then print a string that subtracts 
the start and end times and rounds the value for a "Runtime summary".
'''
#-------------------

# from re import *
#
# pattern = \
# compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
#
# def get_address():
#     address = input('Enter Your Email Address:')
#     is_valid = pattern.match(address)
#     if is_valid:
#         print('Valid Address:', is_valid.group())
#     else:
#         print('Invalid Address! Please Retry...\n')
#
# get_address()

# Enter Your Email Address:local@doamin.tld
# Valid Address: local@doamin.tld

'''
The 're' module allows you to use regex characters to specify a string of characters to use for input. the function 
'get_address()' asks for an email address as input with the 'address' var. if the input matches the regex pattern, 
it is valid and prints a string with the email address. If not, it prints a string asking to retry. The pattern 
variable is a regex expression that is compiled into a pattern object that mimics an email address.
'''
#-------------------

# def display(x):
#     '''Display an argument value.'''
#     print(x)
#
# display(display.__doc__)
#
# display(r'C:\Program Files')
# display('\nDear' +' '+'Stranger,')
# display('Fight for what you believe, always.\n' [:])  # [Starting index : Ending Index]
# display('F' in 'Python')
# display('P' in 'Python')

# Display an argument value.
# C:\Program Files
#
# Dear Stranger,
# Fight for what you believe, always.
#
# False
# True
#

'''
You can manipulate string to display. One way is using a docstring (__doc___). You can also concat and slice bits of 
a string like a list.
'''
#-------------------

# snack = '{} and {}'.format('Burger','Fries')

# print('\nReplaced:',snack)

# Replaced: Burger and Fries

'''
snack var is a formatted string and uses '{}' as placeholders. It passes burger and fries and then prints that string along with 'Replaced:'.
'''

# snack = '{1} and {0}'.format('Burger','Fries')
#
# print('\nReplaced:',snack)

#Replaced: Fries and Burger

'''
By passing the index value for the elements "Burger and fries", you can swap the positions.
'''

# snack = '%s and %s' % ('Milk', 'Cookies')
# print('\nSubstituted:', snack)

'''
This is another way to use formatted strings and placeholders.
'''
#-------------------

string = 'We are who we are.'
# print('\nCapitalized:\t',string.capitalize())
# print('\nTitled:\t\t',string.title())
# print('\nCentered:\t\t',string.center(30,'*'))

# Capitalized:	 We are who we are.
#
# Titled:		 We Are Who We Are.
#
# Centered:		 ******We are who we are.******

# print('\nUppercase:\t', string.upper())
# print('\nJoined:\t\t',string.join('**'))
# print('\nJustified:\t',string.rjust(30,'*'))
# print('\nReplaced:\t',string.replace('s','*'))

# Uppercase:	 WE ARE WHO WE ARE.
#
# Joined:		 *We are who we are.*
#
# Justified:	 ************We are who we are.
#
# Replaced:	 We are who we are.

'''
These are different ways to modify the strings and print them using dot-suffixing.
'''
#-------------------
# import unicodedata
# s = 'Röd'
#
# s = s.encode('utf-8')
# print('\nEncoded String:',s)
# print('Type:',type(s),'\tLength:',len(s))
#
#
# s = s.decode('utf-8')
# print('\nDecoded String:',s)
# print('Type:',type(s),'\tLength:',len(s))

# Encoded String: b'R\xc3\xb6d'
# Type: <class 'bytes'> 	Length: 4
#
# Decoded String: Röd
# Type: <class 'str'> 	Length: 3

'''
You can convert strings to different types of values with encode/decode() methods.
'''

# for i in range(len(s)):
#     print(s[i], unicodedata.name(s[i]), sep=':')

# R:LATIN CAPITAL LETTER R
# ö:LATIN SMALL LETTER O WITH DIAERESIS
# d:LATIN SMALL LETTER D

'''
This iterates through the characters in the string belonging to 's' and prints the character along with its unicode 
name separated by a colon.
'''

# s = b'Gr\xc3\xb6n'
# print('\nGreen String:', s.decode('utf-8'))

# Green String: Grön

'''
This one includes hexadecimal.
'''

# s = 'Gr\N{LATIN SMALL LETTER O WITH DIAERESIS}n'
# print('Green String:', s)
#
# Green String: Grön

'''
This one includes unicode character name.
'''
#-------------------
# file = open('example.txt', 'w')
#
# print('File Name:',file.name)
# print('File Open Mode:', file.mode)
# print('Readable:',file.readable())
# print('Writeable:',file.writable())
#
# def get_status(f):
#     if (f.closed != False):
#         return 'Closed'
#     else:
#         return 'Open'
#
# print('File Status:',get_status(file))
# file.close()
# print('\nFile Status:',get_status(file))

'''
You can open/close and read/write to them as well as get the status of said file(s).
'''
#-------------------

# poem = 'I never saw a man who looked\n'
# poem += 'With such a wistful eye\n'
# poem += 'Upon that little tent of blue\n'
# poem += 'Which prisoners call the sky\n'
#
# file = open('poem.txt','w')
#
# file.write(poem)
# file.close()
#
# file = open('poem.txt','r')
# for line in file:
#     print(line,end='')
# file.close()

'''
This is how you create a txt file named 'poem' and writes a poem to it
and then eventually prints it for the output.
'''
#-------------------

# text = 'The political slogan "Workers Of The World Unite!" is from The Communist Manifesto.'
#
# with open('update.txt','w') as file:
#     file.write(text)
#     print('\nFile Now Closed?:',file.closed)
#
# with open('update.txt','r+') as file:
#     text = file.read()
#     print('\nString:',text)
#
#     print('\nPosition In File Now:',file.tell())
#     position = file.seek(33)
#     print('Position In File Now:',file.tell())

# File Now Closed?: False
#
# String: The political slogan "Workers Of The World Unite!" is from The Communist Manifesto.
#
# Position In File Now: 83
# Position In File Now: 33
#
# Process finished with exit code 0

    # file.write('All lands')
    # file.seek(59)
    # file.write('the tombstone of Karl Marx')
    # file.seek(0)
    # text = file.read()
    # print('\nString:',text)


# File Now Closed?: False
#
# String: The political slogan "Workers Of The World Unite!" is from The Communist Manifesto.
#
# Position In File Now: 83
# Position In File Now: 33
#
# String: The political slogan "Workers Of All lands Unite!" is from the tombstone of Karl Marx

'''
This is how you update file strings and figure out there position.
'''
#-------------------

# import pickle, os
#
# if not os.path.isfile('pickle.dat'):
#     data = [0,1]
#     data[0] = input('Enter Topic:')
#     data[1] = input('Enter Series:')
#     file = open('pickle.dat','wb')
#     pickle.dump(data,file)
#     file.close()
# else:
#     file = open('pickle.dat','rb')
#     data = pickle.load(file)
#     file.close()
#     print('\nWelcome Back To:',data[0],data[1])

# Welcome Back To: Fuck! I have a headache. one

'''
Pickling is pretty much entering input data(objects) and saving it to a binary file that can be later retrieved or 
used in other programs. So here, I imported the pickle module and the os module. if the data file does not already 
exist, create 'pickle.dat'. data is a list of two elements (0 and 1). Then the file open statement for writing to a 
binary file. Then it dumps the pickle data into the file. Then close the file. Else, open 'pickle.dat' and read 
binary. Then it loads the data from the file and then closes it. Finally a string is printed with the input data.
'''
#-------------------

# class ClassName:
    #''' class-doc-string'''
    # class-variable-declarations
    # class-method definitions

# class Snake:
#     ''' A base class for all snake properties. '''
#     count = 0
#     def __init__(self,chat):
#         self.sound = chat
#         Snake.count += 1
#     def talk(self):
#         return self.sound

# HOW TO USE THIS /\

#Create two instances of 'Snake'
# snake1 = Snake('Hiss')
# snake2 = Snake('Sssss')

# Call the talk method from 'Snake'.
# print(snake1.talk())
# print(snake2.talk())

# Print the total number of snake instances
# print(Snake.count)

# output:

# Hiss
# Sssss
# 2

'''
a class is an object that can contain both functions and variables to characterize the object.
class functions = 'methods' ---> class-name.method-name()
class variables = 'attributes' ---> class-name.attribute-name

-'Count' is a class variable that is shared with all instances of the class.
-'__init__()' is how the class is initialized and is automatically called when the class instance is created.
-The '__init__()' initializes an instance variable 'sound' with the value from the 'chat' argument and increments the 
value of the class variable 'count' by 1. 
- The second method, 'talk()' is declared like a regular function, except the first argument is automatically 
included due to it being in a class.
- The 'talk()' method simply returns the value encapsulated in the 'sound' instance variable.
'''
#-------------------

# class Bird:
#     '''A base class to define bird properties.'''
#     count=0
#
# def __init__(self,chat):
#     self.sound = chat
#     Bird.count += 1
#
# def talk(self):
#     return self.sound

# from Bird import *

# print('\nClass Instances Of:\n',Bird.__doc__)
# polly = Bird('Squawk, squawk!')
# harry = Bird('Tweet, tweet!')
#
# print('\nNumber of Birds:', polly.count)
# print('Polly Says:', polly.talk())
#
#
# print('\nNumber of Birds:', harry.count)
# print('Harry Says:', harry.talk())

# Class Instances Of:
# A base class to define bird properties.

# Number of Birds: 1
# Polly Says: Squawk, Squawk!

# Number of Birds: 2
# Harry Says: Tweet, tweet!
'''
I created a class named 'Bird' and imported it into another file. I then printed the document string from bird. I 
then created two instances of the class and named them 'polly' and 'harry' and passed different strings in each of 
them. Then I printed the instance variable(count) and called the class method( talk() ).
'''
#-------------------

# from Bird import *


# chick = Bird('Cheep, cheep!')
# chick.age = '1 week'
#
# print('\nChick Says:',chick.talk())
# print('Chick Age:',chick.age)
#
# chick.age = '2 weeks'
# print('Chick Now:',chick.age)
#
# setattr(chick,'age','3 weeks')
#
# print('\nChick Attributes...')
# for attrib in dir(chick):
#     if attrib[0] != '_':
#         print(attrib,':',getattr(chick,attrib))
#
#
# delattr(chick,'age')
# print('\nChick age Attribute?',hasattr(chick,'age'))

'''
I created an instance of Bird called 'chick' and then used dot notation to add a new attribute [age] and assigned it 
a value, then printed both. I then modified the new attribute to display the new value. I then modified once more but with a built-in function [ setattr() ].
Then I printed a list of all non-private instance attributes and their values using a built in function. For 
attribute in chick, if the first character of the attribute starts with '_', then print the attribute, ':', 
getattr(chick, attrib). Finally, I removed the new attribute and confirmed its removal with a built-in function.
[ delattr() and hasattr() ]
'''
#-------------------

# from Bird import *

# zola = Bird('Beep,beep!')
# print('\nBuilt-in Instance Attributes...')
# for attrib in dir(zola):
#     if attrib[0] == '_':
#         print(attrib)
#
# print('\nClass Dictionary...')
# for item in Bird.__dict__:
#     print(item,':',Bird.__dict__[item])
#
# print('\nInstance Dictionary...')
# for item in zola.__dict__:
#     print(item,':',zola.__dict__[item])

'''
I imported the Bird module nd added a statement to create an instance of 'Bird' named 'zola'.
I then added a loop to display built-in instance attributes. for attribute in directory(zola), if the attribute 
starts with '_', then print the attribute.
Then I added a loop to display all items in the class dictionary.
For item in Bird dictionary, print the item from bird dictionary(item).
Finally, I added a loop to display all items in the instance dictionary.
for item in zola dictionary, print the item from zola dictionary(item).
'''
#-------------------

# See garbage.py and Songbird.py #

# OUTPUT:
# Koko Is Born...
# Koko ID: 2456059903952
# Koko Sings: Tweet, tweet!
#
# Koko Flew Away!
#
# Louie Is Born...
# Louie ID: 2456059903952
# Louie Sings: Chirp, chirp!
#
# Misty Is Born...
# Misty ID: 2456059903760
# Misty Sings: Squawk, squawk!
#
# Louie Flew Away!
#
# Misty Flew Away!

'''
I created a class named 'Songbird' that declares an initializer method
along with two instance variables and prints one of the two variables.
Next, I added a method, 'sing', ti print both variable values.
I then added a delete method that prints the deletion as confirmation.
I then created 'garbage.py' and imported the 'songbird' class.
I then created an instance of songbird named 'bird_1' and had it display its instance attributes.
I then deleted 'bird_1' and created 'bird_2' and 'bird_3', had them display their attributes
and then deleted them.
'''
#-------------------

# SEE Polygon.py / Rectangle.py / Triangle.py
# from Rectangle import *
# from Triangle import *
#
# rect = Rectangle()
# trey = Triangle()
#
# rect.set_values(4,5)
# trey.set_values(4,5)
#
# print('Rectangle Area:',rect.area())
# print('Triangle Area:',trey.area())

# OUTPUT:

# Rectangle Area: 20
# Triangle Area: 10.0

'''
I created a class named 'Polygon' and set the width and height to 0. I then defined two class variables and a method 
to set their values.
I then created a class named 'Rectangle' and passed 'Polygon' as an argument to make it derived. I then defined 
'area' as a method and made it return width multiplied by height.
I then created another class named 'Triangle' and passed 'Polygon' as an argument to make it derived. I then defined
'area' as a method and made it return width multiplied by height divided by 2.
I then imported both 'Rectangle' and 'Triangle' into the bones and created an instance of each derived class ( 'rect' and 'trey' )
I then called both instances and used a class method from 'Polygon' ( .set_values ) and then passed 4 and 5 as 
arguments in the method. Finally, I printed both.

Polygon served as a the base class that provided the method ( set_values ) to both 'Rectangle' and 'Triangle' 
modules, so I was able to manipulate them differently.

Polygon ---> Rectangle / Triangle ---> the bones
'''
#-------------------

# from Man import *
# from Hombre import *
#
# guy_1 = Man('Richard')
# guy_2 = Hombre('Ricardo')
#
#
# guy_1.speak('It\'s a beautiful evening.\n')
# guy_2.speak('Es una tarde hermosa.\n')


# Person.speak(guy_1)
# Person.speak(guy_2)
#
# Richard
# 	Hello! It's a beautiful evening.
#
# Ricardo
# 	Hola! Es una tarde hermosa.
#
# Richard Calling The Base Class
# Ricardo Calling The Base Class

'''
A method can be declared in a derived class to override a matching method in the base class.
I first created a base class, 'Person', that declares an init method to set an instance variable, 'name'.
I then created a second method, 'speak', that prints 'name' along with 'msg'.
I then created a derived class, 'Man' that overrides the second base class method, 'speak', that prints the name, 
a greeting and a short message.
I then created a derived class, 'Hombre', that essentially does the same thing as 'Man', but in spanish.
I then imported both 'Man' and 'Hombre' and created an instance of both derived classes in the bones and named them 
'guy_1' and 'guy_2' and then passed the names, 'Richard' and 'Ricardo' in them.
I then called the overriding methods of each derived class and assigning different values to the 'msg'.
I then called the base class method and passed the derived classes without 'msg', so the default value will be 
displayed, for comparison.
'''
#-------------------

# See 'Duck.py' / 'Mouse.py'

# from Duck import *
# from Mouse import *
#
# def describe(object):
#     object.talk()
#     object.coat()
#
# donald = Duck()
# mickey = Mouse()
#
# describe(donald)
# describe(mickey)

# Duck says: Quack!
#
# Duck wears: Feathers
#
# Mouse Says: Squeak!
#
# Mouse wears: Fur


'''
I first created a class named 'Duck' that declares 2 methods that print a unique string in both.
I then created a class named 'Mouse' that declares 2 methods that also print a unique string in both. ('talk' and 
'coat').
I then imported both 'Duck' and 'Mouse' modules and then defined a function that accepts any single object as its 
argument and then calls the methods of that object.
I then created an instance of each class and named them 'donald' and 'mickey'.
I then called the 'describe' function passed each instance ( 'donald' and 'mickey' ) as an argument.

In short, I created two animals and then made a function that describes the individualized version of the animal and 
then passed the individual in the function. This is because classes can only have one method with a particular name.
'''
#-------------------

# See response.py

'''
This is how you set up a python script to generate an html document.
'''
#-------------------

# from tkinter import *
#
# window = Tk()
# window.title('Label example')
#
# label = Label(window,text='Howdy bish!')
# label.pack(padx=200,pady=50)
#
# window.mainloop()

'''
I am using the 'tkinter' module to create a a GUI. 
I first import 'tkinter' and call a constructor [ Tk() ] to create the 'window' object.
I then specify a title for 'window'.
I then call the 'Label' constructor to create a label for 'window' and set the text to 'Howdy bish!'.
I then call the label with the packer to set the dimensions of the window padding on X/Y - axis.
Finally, I then call the window with the mainloop() to keep the program running.
'''
#-------------------

# from tkinter import *
#
# window = Tk()
# window.title('Button example')
#
# btn_end = Button(window,text='Close',command=exit)
# def tog():
#     if window.cget('bg') == 'yellow':
#         window.configure(bg = 'gray')
#     else:
#         window.configure(bg = 'yellow')
#
# btn_tog = Button(window,text = 'Switch',command=tog)
# btn_tog.pack(padx=150,pady=20)
# btn_end.pack(padx=150,pady=20)
#
#
# window.mainloop()

'''
I first imported tkinter and then created an instance called 'window' and gave it a title called 'Button Example'.
I then created a button called 'btn_end' that has the text of 'close' and takes the command exit.
I then added a function to toggle window's background color when another button is clicked.
tog(): if the window [.cget() = config get] background is yellow, configure the window bg to 'gray'. Else, 
configure the window bg to 'yellow'.
I then created a button to call the function when clicked (btn_tog).
The button (btn_tog) is given the text of 'switch' and takes the toggle command.
I then added the buttons ('btn_tog' and 'btn_end') to the window with packer and passed padding dimensions.
Then I called the window mainloop.
'''
#-------------------

# from tkinter import *
# import tkinter.messagebox as box
#
# window = Tk()
# window.title('Message Box Example')
#
# def dialog():
#     var = box.askyesno('Message Box','Proceed?')
#     if var == 1:
#         box.showinfo('Yes Box','Proceeding...')
#     else:
#         box.showwarning('No Box','Canceling...')
#
# btn = Button(window,text = 'Click',command=dialog)
# btn.pack(padx=150,pady=50)
#
# window.mainloop()

'''
I imported tkinter and the tkinter.messagebox module and set messagebox to the 'box' alias.
I then created 'window' and give it the title, 'Message Box Example'.
I then created a function named 'dialog' to display various message boxes.
I used the 'askyesno' method. When the button is clicked a messagebox pops up and states 'Proceed?' and the
user is given 'yes'' and 'no options.
if 'var' is 1 (yes), the box will show 'Proceeding...'.
else, the box will show 'Canceling...'.
The messagebox icon for 'yes' uses [.showinfo()] and 'no' uses [.showwarning()]
I then created a button to call the function when clicked. (This the first initial button)
I then used the packer with the button to set the padding dimensions and then finally called the window with mainloop.
'''
#-------------------






