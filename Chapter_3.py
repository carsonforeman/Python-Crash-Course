#Introducing Lists

#What is a list? 

#a collection of items in particular order using square brackets []

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print (bicycles)

#Accessing Elements in a List

#lists are ordered collections you can access by telling Python the index or position. 

print (bicycles[0])

#You can also use string methods on any elemnts in the list. 

print (bicycles[0].title())

#index positions start at 0 not 1

print(bicycles[-1]) #returns the last item in the list. 

#Using individual values from a List

message = f"My first bicycle was a {bicycles[0].title()}."
print (message)

#Changing adding or Removing Elements
	#most lists will be dynamic meaning they will change (add/remove items)

#modifying elements

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print (motorcycles)


#Adding Elements To a List
	#new data always needs to be added

#appending elements to end of list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

#you can use append to build lists dynamically

motorcyles = []
motorcyles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print (motorcycles)

#inserting elements into a list
#You can add to any position in a list using insert() metho. 

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

#Removing Elements From a List
#using del statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print ( motorcycles)

del motorcycles[0]
print (motorcycles)

#Removing an Item Using the pop() Method 
#pop removes an item but lets you still work with it, if you need the data. 
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#Popping Items from any position 

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first I owned was a {first_owned.title()}.")


#Removing an Item by Value
	#You don't know the position but you know the name/value

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.remove('honda')

#To work with value you remove

motorcycles = ['honda', 'yamaha', 'suzuki']
too_expensive = 'honda'
motorcycles.remove(too_expensive)

#Organizing A List
#sometimes data is bad so list is not structured right. 

#Sorting a list Permanantely with sort() method
#puts in alphabetical order
#put in reverse alphabetical order by passing argument reverse = true
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print (cars)

cars.sort(reverse=True)
print (cars)

#To present in sorted order without changing permanetnaly use sorted() function.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print ('Here is the original list:')
print (cars)

print ('Here is the sorted list:')
print (sorted(cars))

print ('Here is the original list again:')
print (cars)

#Printing a List in Reverse Order
#to reverse the order of a list. 

cars = ['bmw', 'audi', 'toyota', 'subaru']
print (cars)

cars.reverse()
print (cars)

#finding the length of a list

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
