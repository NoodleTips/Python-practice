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
#     balance = function_1() #? Start thinking of something or someone. A book, waffle-iron, your cat, a group of cats,
#                            #? a type of cat, etc...
#     lines = get_number_of_lines()  #^^^^ Once you think of something or a goal.
#                                    #^^^^ Think about the features, the individual parts, the next sub level down from
#                                    #^^^^ the goal. Stick these parts under main()
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

i = 1
while i < 4:
    print('\nOuter Loop Iteration:,', i)
    i += 1
    j = i
    while j < 4:
        print('\tInner Loop Iteration:'.j)
        j += 1






