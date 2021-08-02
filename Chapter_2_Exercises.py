#2-3. Personal Message: Use a variable to represent a person’s name, and print
#a message to that person. Your message should be simple, such as, “Hello Eric,
#would you like to learn some Python today?”

person = 'Chris Fitch'
question = 'Do you think you might have fully lost it?'

print (f"Hey {person}! {question}")

#2-4. Name Cases: Use a variable to represent a person’s name, and then print
#that person’s name in lowercase, uppercase, and title case.

name = 'carson foreman'

print (name.upper())
print (name.lower())
print (name.title())

#2-5. Famous Quote: Find a quote from a famous person you admire. Print the
#quote and the name of its author. 

author = 'George Orwell'
quote = '"All animals are equal, but some animals are more equaler than others."'

print (f"{author} once said, {quote}")

#2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the
#famous person’s name using a variable called famous_person. Then compose
#your message and represent it with a new variable called message. Print your
#message.

famous_person = 'George Orwell'
quote = '"All animals are equal, but some animals are more equaler than others."'

message = (f"{famous_person} once said, {quote}")
print (message)


#2-7. Stripping Names: Use a variable to represent a person’s name, and include
#some whitespace characters at the beginning and end of the name. Make sure
#you use each character combination, "\t" and "\n", at least once.
#Print the name once, so the whitespace around the name is displayed.
#Then print the name using each of the three stripping functions, lstrip(),
#rstrip(), and strip().

name = ' \n\tcarson foreman ' 
print (name)
print (name.strip())
print (name.rstrip())

#2-8. Number Eight: Write addition, subtraction, multiplication, and division
#operations that each result in the number 8. Be sure to enclose your operations
#in print() calls to see the results. 

print (5+3)
print (10-2)
print (4*2)
print (16/2)

#2-9. Favorite Number: Use a variable to represent your favorite number. Then,
#using that variable, create a message that reveals your favorite number. Print
#that message.

favorite_number = 5 

message = f"My favorite number is {favorite_number}."
print (message)