#3-1. Names: Store the names of a few of your friends in a list called names. Print
#each person’s name by accessing each element in the list, one at a time

names = ['chris','chim','sean', 'joe', 'evan']
print (names[0])
print (names[1])
print (names[2])
print (names[3])
print (names[4])


#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
#printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the
#person’s name. 

names = ['chris','chim','sean', 'joe', 'evan']
message = f"Hey, {names[0].title()}, do you want to meet at Eden tonight?"
print (message)
message = f"Hey, {names[1].title()}, do you want to meet at Eden tonight?"
print (message)

#3-3. Your Own List: Think of your favorite mode of transportation, such as a
#motorcycle or a car, and make a list that stores several examples. Use your list
#to print a series of statements about these items, such as “I would like to own a
#Honda motorcycle.”

cars = ['BMW', 'Toyota', "Tesla"]
dream = f"I would like to own a {cars[-1]} but right now I have a {cars[1]}."
print (dream)


#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
#would you invite? Make a list that includes at least three people you’d like to
#invite to dinner. Then use your list to print a message to each person, inviting
#them to dinner.

guest_list = []

guest_list.append('michael jordan')
guest_list.append('george orwell')
guest_list.append('nikola tesla')

print (f'Hey, {guest_list[0].title()}, you are invited to a private dinner!')
print (f'Hey, {guest_list[1].title()}, you are invited to a private dinner!')
print (f'Hey, {guest_list[2].title()}, you are invited to a private dinner!')

#3-5. Changing Guest List: You just heard that one of your guests can’t make the
#dinner, so you need to send out a new set of invitations. You’ll have to think of
#someone else to invite.
#•	 Start with your program from Exercise 3-4. Add a print() call at the end
#of your program stating the name of the guest who can’t make it.
#•	 Modify your list, replacing the name of the guest who can’t make it with
#the name of the new person you are inviting.
#•	 Print a second set of invitation messages, one for each person who is still
#in your list.

guest_list = []

guest_list.append('michael jordan')
guest_list.append('george orwell')
guest_list.append('nikola tesla')

print ("Hey everyone, it turns out Michael Jordan can't make it to dinner!")
guest_list[0]='john f kennedy'
print (guest_list)


#3-6. More Guests: You just found a bigger dinner table, so now more space is
#available. Think of three more guests to invite to dinner.
#•	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
#call to the end of your program informing people that you found a bigger
#dinner table.
#•	 Use insert() to add one new guest to the beginning of your list.
#•	 Use insert() to add one new guest to the middle of your list.
#•	 Use append() to add one new guest to the end of your list.
#•	 Print a new set of invitation messages, one for each person in your list.

guest_list = []

guest_list.append('michael jordan')
guest_list.append('george orwell')
guest_list.append('nikola tesla')

print ("Hey everyone, it turns out Michael Jordan can't make it to dinner!")
guest_list[0]='john f kennedy'
print (guest_list)

print ('Hey everyone we found a bigger table!')
guest_list.insert(0,'patti foreman')
guest_list.insert(2,'abe lincoln')
guest_list.append('albert einstein')

print (f"Hey, {guest_list[0].title()}, you are invited to the new dinner!")
print (f"Hey, {guest_list[1].title()}, you are invited to the new dinner!")
print (f"Hey, {guest_list[2].title()}, you are invited to the new dinner!")
print (f"Hey, {guest_list[3].title()}, you are invited to the new dinner!")
print (f"Hey, {guest_list[4].title()}, you are invited to the new dinner!")
print (f"Hey, {guest_list[5].title()}, you are invited to the new dinner!")


#3-7. Shrinking Guest List: You just found out that your new dinner table won’t
#arrive in time for the dinner, and you have space for only two guests.
#•	 Start with your program from Exercise 3-6. Add a new line that prints a
#message saying that you can invite only two people for dinner.
#•	 Use pop() to remove guests from your list one at a time until only two
#names remain in your list. Each time you pop a name from your list, print
#a message to that person letting them know you’re sorry you can’t invite
#them to dinner.
#•	 Print a message to each of the two people still on your list, letting them
#know they’re still invited.
#•	 Use del to remove the last two names from your list, so you have an empty
#list. Print your list to make sure you actually have an empty list at the end
#of your program.

guest_list = []

guest_list.append('michael jordan')
guest_list.append('george orwell')
guest_list.append('nikola tesla')

print ("Hey everyone, it turns out Michael Jordan can't make it to dinner!")
guest_list[0]='john f kennedy'
print (guest_list)

print ('Hey everyone we found a bigger table!')
guest_list.insert(0,'patti foreman')
guest_list.insert(2,'abe lincoln')
guest_list.append('albert einstein')

print ("Sorry but I can actually only have 2 people over for dinner!")
popped_0 = guest_list.pop(0)
print (f"Hey sorry {popped_0.title()} but you can't come to dinner!")
popped_1 = guest_list.pop(1)
print (f"Hey sorry {popped_1.title()} but you can't come to dinner!")


#3-8. Seeing the World: Think of at least five places in the world you’d like to
#visit.
#•	 Store the locations in a list. Make sure the list is not in alphabetical order.
#•	 Print your list in its original order. Don’t worry about printing the list neatly,
#just print it as a raw Python list.
#•	 Use sorted() to print your list in alphabetical order without modifying the
#actual list.
#•	 Show that your list is still in its original order by printing it.
#•	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
#•	 Show that your list is still in its original order by printing it again.
#•	 Use reverse() to change the order of your list. Print the list to show that its
#order has changed.
#•	 Use reverse() to change the order of your list again. Print the list to show
#it’s back to its original order.
#•	 Use sort() to change your list so it’s stored in alphabetical order. Print the
#list to show that its order has been changed.
#•	 Use sort() to change your list so it’s stored in reverse alphabetical order.
#Print the list to show that its order has changed.

places = []
places.append('rome')
places.append('vegas')
places.append('canada')
places.append('brazil')
places.append('sweden')
print (places)

print (sorted(places))
print (places)
print (sorted(places, reverse = True))
print (places)
places.reverse()
print (places)
places.sort()
print (places)
places.sort(reverse = True)
print (places)

#3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
#through 3-7 (page 42), use len() to print a message indicating the number
#of people you are inviting to dinner.

guest_list = []

guest_list.append('michael jordan')
guest_list.append('george orwell')
guest_list.append('nikola tesla')
print (guest_list)
print (f"The number of people in the dinner guest list is {len(guest_list)}!")

#3-10. Every Function: Think of something you could store in a list. For example,
#you could make a list of mountains, rivers, countries, cities, languages, or anything 
#else you’d like. Write a program that creates a list containing these items
#and then uses each function introduced in this chapter at least once.

proteins = []
proteins.append('chicken')
proteins.append('steak')
proteins.append('tofu')
proteins.append('beans')
proteins.append('fish')

print(proteins)
print(proteins[0])
print(proteins[0].title())
print(f"If you are a vegetarian you can have the {proteins[2]}!")
proteins[4]='salmon'
print(proteins)
proteins.append('seitan')
print(proteins)
del(proteins[5])
print(proteins)
proteins.sort()
print(proteins)
proteins.sort(reverse=True)
print(proteins)
print(sorted(proteins))