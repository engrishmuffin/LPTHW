# cheese_and_crackers prints cheese_count and
# boxes_of_crackers variables in a paragraph
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man, that's enough for a party!"
    print "Get a blanket.\n"

# define variables as raw numbers within argument.
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

# define variables as other variables
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
# cheese_count = amount_of_cheese, etc.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# define variables with equations as arguments
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# define vars with arguments that combine vars and numbers
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def partytime(invites, rooms, hours, snacks, drinks):
    print "Let's throw a party!"
    print "We'll invite %r people." % invites
    print "We can open up %r rooms in the house." % rooms
    print "We can have people over for %r hours." % hours
    print "We will need %r snacks for everyone." % snacks
    print "And we should probably get about %r drinks." % drinks

partytime(10, 3, 4, 6, 20)

roommates = 4
invites = roommates * 5
partytime(invites, 3 + roommates / 4, 3 + roommates / 4 * 2, 3 + roommates / 4 * invites, 3 + roommates / 4 * invites * 2)

# prompt = "\n>"
# print "how many people live in your house?"
# int roommatesa = raw_input (prompt)
# int invitesa = 5 * roommates2
# int spacea = 3 + roommates2
# int timea = 3 + roommates2 / 4 * 2
# int fooda = 3 + roommates2 / 4 * invites2
# int drinksa = 3 + roommates2 / 4 * invites2 * 2
#
# partytime(invitesa, spacea, timea, fooda, drinksa)
