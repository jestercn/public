#! /usr/bin/python
print("how are you")
print("goodbye")
message1 = "Hello pYTHON world"
print(message1.lower())
print(message1)
message2 = "hello python crash course world"
print(message2.upper())
message3 = message1 + " " + message2
print(message3.title())
print('I told my friend,"Python is my favorite language!"')
print("I told my friend,'Python is my favorite language!'")
print("Hello, " + message3.title() + " !")
message4 = "hello, " + message3.title() + " !"
print(message4)
print("\tPython")
print("Python\t\t\tis a language")
print("language:\n\tpython\n\tjavascript")
favorite_language = "python "
print(favorite_language + message4)
print(favorite_language.rstrip() + message4)
my_name = 'zheng yi ming'
print(my_name.lower())
print(my_name.title())
print(my_name.upper())
print(my_name)
print("\tzheng yi ming")
print("\tzheng\n\t yi\n\t ming")
blank = " how are you "
print(blank)
print(blank.lstrip())
print(blank.strip())
age = 23
print("Happy " + str(age) + "rd birthday")
bicycles = [ 'trek', 'cannondale','redline']
print(bicycles)
print(bicycles[1])
print(bicycles[1].upper())
print(bicycles[-1])
message_bicycle = "My first bicycle was a " + bicycles[1].title() + "."
print(message_bicycle)
bicycles[1]='fenghuang'
print(bicycles)
bicycles.append('jieante')
print(bicycles)
bicycles.insert(0, 'hongqi')
for bicycle in bicycles :
	print(bicycle)
print(bicycles)
del bicycles[2]
print(bicycles)
poped_bicycles = bicycles.pop()
print(bicycles)
print(poped_bicycles)
second_owned = bicycles.pop(1)
print('The second bicycle I owned was a ' + second_owned.title() +' .')
print(bicycles)
too_low = 'hongqi'
bicycles.remove(too_low)
print(bicycles)
print("\nA " + too_low.title() + "is too low.")
bicycles.insert(0, 'you')
bicycles.insert(0, 'are')
bicycles.insert(0, 'how')
print(bicycles)
bicycles.sort()
print(bicycles)
bicycles.sort(reverse=True)
print(bicycles)
print(sorted(bicycles))
print(bicycles)
bicycles.reverse()
print(bicycles)
bicycles.reverse()
print(bicycles)
print(len(bicycles))
for bicycle in bicycles :
	print(bicycle)
bicycles.reverse()
for bicycle in bicycles :
	print(bicycle)
for value in range(1,6):
	print(value)
numbers = list(range(1,10))
print(numbers)
numbers = list(range(1,20,2))
print(numbers)
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)
goods = []
for value in range(1,20):
	goods.append(value**2)
print(goods)
print(min(goods))
print(max(goods))
print(sum(goods))

seeds = [value**2 for value in range(1,11)]
print(seeds)
print(seeds[0:3])
print(seeds[-3:])
print(seeds[:5])
print(seeds[1:5])
print(seeds[:-1])
print(seeds[-1:])
print(seeds[0:-3])
for seed in seeds[:]:
	print(seed)
foods = seeds[:]
print("\nMy friends favorite foods are:")
print(foods)
foods.append(121)
print(seeds)
print(foods)
sexys = foods[2:-1]
print(sexys)
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions :
	print(dimension)
dimensions = (400,100,800)
for dimension in dimensions :
	print(dimension)
cars = [ 'audi','bmw','subaru','toyota']
for car in cars :
	if car == 'bmw' :
		print(car.upper())
	else :
		print(car.title())
dogs = ['jinmao','caiquan','haqishi','shamoye']
if 'jinmao' in dogs :
	print("jinmao dog in the list")
else :
	print("jinmao dog not in the list")
if 'tugou' not in dogs :
	print("tugou dog not in the list")
else :
	print("tugou dog in the list")
if (3 > 2) and (5 > 6) :
	print("right")
else :
	print("wrong")
my_age = 12
if my_age < 4 :
	print("your admission cost is $0.")
elif my_age <18 :
	print("your admission cost is $5.")
else :
	print("your admission cost is $10.")
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)
for number in range(3) :
	message5 = input("Tell me something ,and I will repeat it back to you!\n")
	print(message5)
current_number = 2
while current_number <= 5:
	print(current_number)
	current_number += 1
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active :
	message = input(prompt)
	if message == 'quit' :
		active = False
	else :
		print(message)


	
	
	
	








