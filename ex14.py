from sys import argv
#Requires argument on launch... give it a name.
script, user_name, classification = argv
prompt = 'TYPEYOURWORDSHEREMEATSACK!!!!'
#greets user, define script.
print "Hi %s: %s, I'm the %s script." % (classification, user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me, %s?" % user_name
likes = raw_input (prompt)

print "Where do you live, %s?" %user_name
lives = raw_input (prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)
#Prints contextualized raw_input in order.
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice
""" % (likes, lives, computer)
