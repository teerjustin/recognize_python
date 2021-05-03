
# data type Numbers(int)
num1 = 42


# data type float
num2 = 2.3

# data type Boolean
boolean = True

# data type String
string = 'Hello World'

#list
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#dictionary
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#tuple
fruit = ('blueberry', 'strawberry', 'banana')
#access value tuple
print(type(fruit))
#access value list
print(pizza_toppings[1])
#create value list
pizza_toppings.append('Mushrooms')
#acess value dictionary
print(person['name'])
#change value dictionary
person['name'] = 'George'
#add value dictionary 
person['eye_color'] = 'blue'
#access value list
print(fruit[2])


# conditionals
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")


# for loop
for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
# while loop
while(x < 5):
    print(x)
    x += 1
# delete value olives
pizza_toppings.pop()
#delete value  sausage
pizza_toppings.pop(1)

print(person)
#delete value eye_color
person.pop('eye_color')
print(person)

#for loop (prints "After 1st if statement 4 times")
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

#functiion -> for loop (prints 10 times)
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

#function -> for loop prints(x times ( in this case 4))
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

#function -> for loop prints(10 + 4 times)
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)