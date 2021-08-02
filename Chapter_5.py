#If Statements 

#A Simple Example 

#Imagine you want to capitalize the names of cars in list 
#but you want bmw to print in all capitals: 

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
 		print(car.upper())
	else:
 		print(car.title())

 #Conditional Test

 	#at the heart of all if statemtents are conditional tests (true or false)

 	#checking for equality 
 		#most conditional tests comparet the current value to a value of iterest: 
 		car = 'bmw'
 		car == 'bmw'
 		#true #double equals is the equality operator 
 		#testing for eqaulity is case sensitive

 	#checking for inequality 
 	#use != to check if not equal 

 	#requested_topping = 'mushrooms'
 	#if requested topping != 'anchiovies':
 		#print ("Hold the anchovies!")

 	#Numerical Comparisons 

 	#age = 18
 	#age == 18 
 	#True 

 	#You can also check if numbers are not equal and also you can use <, >, and <=. 

 	#Checking Multiple Conditions 

 	#use and / or to check multiple conditions 

 	#Using and to check multiple conditions 
 		#if either test fails fails the expression is false
 		#ex: age_0 = 22, age_1 = 18 
 			#age_0 and age_1 >= 21 
 			# false 

 	#Using or to Check Multiple Conditions 

 		#passes if either or both are true


 	#Checking Whether a Value is in a LIst
 		#checking if a username is in a list before new registrations (for example)
 		>>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
		>>> 'mushrooms' in requested_toppings
			True
		>>> 'pepperoni' in requested_toppings
			False

	#Checking Whether a Value is Not in a list 
		#if user not in banned_users: 
			#print ()

		#Boolean Expressions
		#boolean is just another term for conditional a bloolean value is either true or false

		#If Statements

			#Simple If statemtents
				#The simplest test has one test and one action 
				#if conditional test: 
					#do something

				#age = 19 
				#if age>=18:
					#print("You are old enough to vote.")

			#indentation is used in if statements 
			#you can have as many lines of code folliwing the if statement.
      
      #if-else Statements 
      	#take one action or another depending on conditional test
			#age =17
			#if age >= 18:
				#print("you are old enough")
			#else: 
				#Pring("sorry you are too young")

	#The if-elif-else Chain 
		#used to test more than two possible siutations 
		#Python executes only one block ones a test passes. 
		#consider: admission is free under 4 years old
				   #4 to 18 pays 25 dollars 
				   #18 and up pays $40
				   	#age = 12
				   	#if age < 4: 
				   		#print("your free")
				   	#elif age < 18:
				   		#print(25 dollars)
				   	#else:
				   		#print(you pay 40 dollars)
				#it would be more consise to place the price in
				#the chain of code and have one print statement at the end. 

	#Using Multiple elif Blocks 
		#you can have multiple elif lines between the if and else statements

	#OMitting the else block 
		#python doesn't require the else block at the end of the chain. 
		#sometimes you can just use elif statements. 

	#Testing Multiple Conditions 
	#sometimes you want python to check mutliple tests and not stop 
	#after one test is satified so you can use multiple if statements. 
		#requested_toppings = ['mushrooms', 'extra cheese']
		#if 'mushrooms' in requested_toppings:
			#print("adding mushrooms")
		#if 'pepperoni' in requested_toppings: etc. 


#Using if Statements with Lists

	#YOu can do interesting things combining lists and if statements. YOu can manage changing condittions easily. 

#Checking for special items
	#Remember how "bmw" had to be in all caps. LEts look at another example. 
		#requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
		#for requested_topping in requested_toppings:
 			#print(f"Adding {requested_topping}.")
		#print("\nFinished making your pizza!")    #THIS IS A SIMPLE FOR LOOP BUT WHAT IF WE RUN OUT OF TOPPING

							#we add a line that says if rquested_topping == 'green peppers' print sorry we are out. 

#Checking that a list is not empty

	#we can't assume a list has values. We must check: 

		#requested_toppings = []
		# if requested_toppings:
 			#for requested_topping in requested_toppings:
 				#print(f"Adding {requested_topping}.")
 			#print("\nFinished making your pizza!")
			#else:
 			#print("Are you sure you want a plain pizza?")

 #Using Multiple Lists
 	#what if a person orders a topping for a pizza that isn't in the list. 
 	# we can work with two lists which are 1. the toppings we have 2. the toppings customer requests
 	#available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
	#requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
	#for requested_topping in requested_toppings:
		#if requested_topping in available_toppings:
 			#print(f"Adding {requested_topping}.")
	#else:
 		#print(f"Sorry, we don't have {requested_topping}.")

	#print("\nFinished making your pizza!")


#

