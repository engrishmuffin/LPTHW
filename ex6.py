#Define the variable "x" a string which is the setup for a joke
x = "There are %d types of people." % 10
#Define first string variable to insert into punchline string
binary = "binary"
#Define second string variable to insert into punchline string.
do_not = "don't"
#Define String variable for punchline string.
y = "Those who know %s and those who %s." % (binary, do_not)

#Print Setup of joke
print x
#Print Punchline of joke
print y

#These two lines reiterate the joke to a reader who obviously doesn't get it.
print "I said: %r." % x
print "I also said: '%s.'" % y

#Define the response variable for the joke's hilarity.
hilarious = False
#Define string variable for eliciting and receiving a response, call a %r variable.
joke_evaluation = "Isn't that joke so funny?! %r"
#print the joke evaluation string and name the variable call - hilarious
print joke_evaluation % hilarious

#Define two string variables that together will make a sentence.
w = "This is the left side of..."
e = "a string with a right side."
#Print the two variables together on the same line to make a sentence.
print w + e
print w, e
