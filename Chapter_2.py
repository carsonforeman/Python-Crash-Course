print("Hello Python world!")

message = "Hello Python world!"
#variable is message 
#value is hello python world 
print (message)

message = "Hello Python Crash Course world!"
print (message)

message = "Hello Python Crash Course reader!"
print (message)

#Try It Yourself 

#2-1 Simple Message: Assign a message to a variable and print that message. 

plan = "Carson will take over the world"
print (plan)

#2-2. Simple Messages: Assign a message to a variable, and print that message.
#Then change the value of the variable to a new message, and print the new
#message.

mission = "To learn python"
print (mission)
mission = "to learn python fluently"
print (mission)

#String is a series of characters in quotes, single or double. 

#Changing case in a string with method
#the . after the variable tells the method act on it. 

name = "carson foreman"
print (name.title())
print (name.upper())
print (name.lower())

#Using variables in strings

first_name = "carson"
last_name = "foreman"
full_name = f"{first_name} {last_name}"
print (full_name)

#this is an example of an fstring (format)

print(f"Hello, {full_name.title()}!")

#Adding Whitespace to Strings with Tabs or Newlines

#\t adds a tab

print("Python")
print("\tPython")

#\n starsts a new line

print("Languages:\nPython\nC\nJavascript")

#Stripping Whitespace

#this is temporary

favorite_language = 'python '
print (favorite_language)
favorite_language.rstrip()
print (favorite_language)

#to make it permanate you must reassign the variable

favorite_language = favorite_language.rstrip()
print (favorite_language)

#You can alaso use lstrip() or strip() to strip left side or both sides of whitespace. 


#Numbers

#You can add, subtract, multiply, and dive in Python

print (2+4)

#floats are numbers with a decimal point 

#integers and floats

print (4/2) 
#returns 2.0

#Underscores in numbers
#use to make more readable

universe_age = 14_000_000_000
print (universe_age)

#multiple assignment

x, y, z = 0, 0, 0 
print (x)
print (y)
print (z)
print(x,y,z)


#use all caps in variable name to indicate a constant whose value shouldn't be changed. 

MAX_CONNECTIONS = 5000

#Comments
#use hashtags to write comments 