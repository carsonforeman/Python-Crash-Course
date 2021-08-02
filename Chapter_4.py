#Chapter 4 Working with Lists

#Looping Through a List
#faster way to retrieve information from a list 

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)


#A Closer Look at Looping 
	#python will loop through list until completetion
	#you can name the temporary variable anything you want. 

#Doing more work within a for loop
	#lets print a message to each magician 

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
		print (f"{magician.title()}, that was a great trick!")
#You can write as many lines you want inside the for loop. 

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
		print (f"{magician.title()}, that was a great trick!")
		print(f"I can't wait to see your next trick, {magician.title()}.\n")

#Doing Something After a for Loop
	#any lines after the for loop are executed once

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
		print (f"{magician.title()}, that was a great trick!")
		print(f"I can't wait to see your next trick, {magician.title()}.\n")
print ("Thank you, everyone. That was a great magic show!")

#Avoiding Indentation Errors
	#indentation in for loop are easy to read
	#forgetting to indent
		#always indent after for statement
		#always indent each line in a the for loop (code is valid but still wrong)
	#accidental indentation
		#indenting print statement is an error. 
		#after loop will print for every item in the list. 
	#forgetting the colon
		#colon at the end of for statement or youll get an error. 


#Making numberical lists
	#Many reasons exist to store numbers in lists (position of character in game for example)

#Using the range() function
	#generates a series of numbers 
	#for value in range(1,5): 

#Using range to make a list of numbers

#numbers = list(range(1,6))

#if you pass a third argument to range python uses it as a step 
	#even_numbers = list(range(2,11,2))

#Simple Statistics with a list of Numbers
	#digits = [1,2,3,4,5,6,8,9,0]
	#min(digits)
	#max(digits)
	#sum(digits)

#list comprehensions

#build a list of the first 10 squares, this combines the for loop and new elements into one line. 

	#squares = [value**2 for value in range(1,11)]
	#print (squares)

#Working With Part of a List

	#Slicing a LIst 
	#To make a slice you specify the first and last elements you want 
	#ex print(players[0:3])
	#print(players[2:]) would go to end of list 
	#print(players[-3]) would give the last 3 players

#Looping Through a Slice
#You can use a slice in a for loop if you want to loop through a subset of the elements in a list. 

#players = ['charles', 'martina', 'michael', 'florence', 'eli']
#print("Here are the first three players on my team:")
#for player in players[:3]:
 #print(player.title())

#Copying a List 

#to make a copy of a list take a slice without any index: my_foods = friends_foods[:]


#Tuples 

#lists are good for items that cna change. Tuples allow immutable lists that change. 

#defining a tuple 
	#Tuples look like lists except you use parantheses. 
	#for example a rectangles dimensions: 
	#dimensions = (200, 50)

#Looping through all values in a tuple 
	#you can loop through tuples same as lists

#Writing over a tuple 
	#although you can't modify a tuple you can change the value of the variable that represents the tuple. 
	#dimensions = (200,50)
	#dimensions = (400, 100)

#4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
#simple foods, and store them in a tuple.
#Use a for loop to print each food the restaurant offers.
#Try to modify one of the items, and make sure that Python rejects the
#change.
#The restaurant changes its menu, replacing two of the items with different
#foods. Add a line that rewrites the tuple, and then use a for loop to print
#each of the items on the revised menu.

buffet_foods = ('eggs', 'bacon', 'sausage', 'pancakes', 'oatmeal')
for food in buffet_foods:
	print (food)
buffet_foods = ('eggs', 'bacon','sausage','waffles','grits')
for food in buffet_foods:
	print (food)
