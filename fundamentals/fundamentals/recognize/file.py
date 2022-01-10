num1 = 42 # variable declaration, initialize number
num2 = 2.3 # variable declaration, initialize number
boolean = True # variable declaration, initialize boolean
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, initialize tuple
print(type(fruit)) # log statement, type check
print(pizza_toppings[1]) # log statement, access list value
pizza_toppings.append('Mushrooms') # add list value
print(person['name']) # log statement, access dictionary value
person['name'] = 'George' # change dictionary value
person['eye_color'] = 'blue' # add dictionary value
print(fruit[2]) # log statement, access tuple value

if num1 > 45: # conditional if
    print("It's greater") # log statement
else: # conditional else
    print("It's lower") # log statement

if len(string) < 5: # conditional if, length check
    print("It's a short word!") # log statement
elif len(string) > 15: # conditional else if, length check
    print("It's a long word!") # log statement
else: #conditional else
    print("Just right!") # log statement

for x in range(5): # for loop start
    print(x) # log statement
for x in range(2,5): # for loop start stop
    print(x) # log statement
for x in range(2,10,3): # for loop start stop increment
    print(x) # log statement
x = 0 # variable declaration, initialize number
while(x < 5): # while loop start
    print(x) # log statement
    x += 1 # increment

pizza_toppings.pop() # delete list value
pizza_toppings.pop(1) # delete list value

print(person) # log statement
person.pop('eye_color') # delete dictionary value
print(person) # log statement

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni': # conditional if
        continue # continue
    print('After 1st if statement') # log statement
    if topping == 'Olives': # conditional if
        break # break

def print_hello_ten_times(): # function definition
    for num in range(10): # for loop start
        print('Hello') # log statement

print_hello_ten_times() # function call

def print_hello_x_times(x): # function definition, parameter
    for num in range(x): # for loop start
        print('Hello') # log statement

print_hello_x_times(4) # function call, argument pass

def print_hello_x_or_ten_times(x = 10): # function definition, default parameter
    for num in range(x): # for loop start
        print('Hello') # log statement

print_hello_x_or_ten_times() # function call
print_hello_x_or_ten_times(4) # function call, argument pass


""" multiline comment
Bonus section
"""
# single-line comment
# print(num3) # NameError
# num3 = 72 # variable declaration, initialize number
# fruit[0] = 'cranberry' # TypeError, tuple value change
# print(person['favorite_team']) # log statement, access dictionary value, KeyError
# print(pizza_toppings[7]) # log statement, access list value, IndexError
#   print(boolean) # log statement, IndentationError
# fruit.append('raspberry') # AttributeError, add tuple value
# fruit.pop(1) # AttributeError, remove tuple value