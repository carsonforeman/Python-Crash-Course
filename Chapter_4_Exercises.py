#4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
#pizza names in a list, and then use a for loop to print the name of each pizza.
#•	 Modify your for loop to print a sentence using the name of the pizza
#instead of printing just the name of the pizza. For each pizza you should
#have one line of output containing a simple statement like I like pepperoni
#pizza.
#•	 Add a line at the end of your program, outside the for loop, that states
#how much you like pizza. The output should consist of three or more lines
#about the kinds of pizza you like and then an additional sentence, such as
#I really love pizza!

pizzas = []
pizzas.append('cheese')
pizzas.append('bbq chicken')
pizzas.append('ham and pineapple')

for pizza in pizzas:
	print (pizza)

for pizza in pizzas: 
	print (f"I like {pizza.title()} Pizza alot!")
print ("I really like pizza in general it doesn't really matter what kind!")

#4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to
#print out the name of each animal.
#•	 Modify your program to print a statement about each animal, such as
#A dog would make a great pet.
#•	 Add a line at the end of your program stating what these animals have in
#common. You could print a sentence such as Any of these animals would
#make a great pet!

pets = ['dog', 'cat', 'rabbit']

for pet in pets:
	print (pet)

for pet in pets: 
	print (f"A {pet} would make a good pet!")
print ("All of these animals would really make a good pet!")


#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive. 

numbers = [value for value in range(21)]
print (numbers)

numbers = list(range(21))

for value in numbers:
	print (value)

#4-4 One Million: Make a list of the numbers from one to one million and use a for loop to print
#the numbers. (stop with cntrol-C). 

long_list = list(range(1000))

for value in long_list:
	print (value)

#4-5:  Summing a Million: Make a list of numbers from 1 to million and use min, max to check. Use sum. 

long_list = list(range(1000001))
print(min(long_list))
print(max(long_list))
print(sum(long_list))

#4-6: Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers
#from 1 to 20, Use a for loop to print each number. 

odd_numbers = list(range(1,21,2))
for number in odd_numbers:
	print(number)

#4-7: Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers
#in your list. 

multiples = list(range(3,31,3))
for number in multiples:
	print (number)

#4-8: Cubes: A number raised to the third power is called a cube. For example the cube of 2 
#is written as 2**3 in Python. Make a list of the first 10 cubes and use a for loop to print 
#the value of each cube. 

cubes = []

for number in range(11):
	cube = number**3
	cubes.append(cube)

for cube in cubes:
	print (cube)

#4-9: Cube Comprehension: Use a list comprehnsion to generate a list of the first 10 cubes. 

cubes = [number**3 for number in range(11)]
print (cubes)

#4-10: Slices: Using one of the programs add several lines that: 
##Print the message The first three items in the list are:. Then use a slice to
#print the first three items from that program’s list.

#Print the message Three items from the middle of the list are:. Use a slice to
#print three items from the middle of the list

#Print the message The last three items in the list are:. Use a slice to print the
#last three items in the list.

multiples = list(range(3,31,3))
for number in multiples:
	print (number)

print ("The first three items in the list are:")
for value in multiples[:3]:
	print (value)

#4-11: My Pizzas, Your Pizzas: Start with your program from 4-1
#Make a copy of the list of pizzas and call it friend_pizzas. then: 

#Add a new pizza to the original list.
#Add a different pizza to the list friend_pizzas.
#Prove that you have two separate lists. Print the message My favorite
#pizzas are:, and then use a for loop to print the first list. Print the message
#My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
#Make sure each new pizza is stored in the appropriate list.

pizzas = []
pizzas.append('cheese')
pizzas.append('bbq chicken')
pizzas.append('ham and pineapple')

friend_pizzas = pizzas[:]

print (friend_pizzas)

pizzas.append('spinach')
friend_pizzas.append('mushroom')

print ("My favorite pizzas are:")
for pizza in pizzas: 
	print (pizza)
print ("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print (pizza)