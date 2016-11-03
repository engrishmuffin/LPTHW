from sys import argv
# define the target of this script in argv
script, filename = argv
# Give instructions to user.
print "we're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit Return."
#Prompt user to proceed or close script.
raw_input("?")
# Update user and open file.
print "Opening the file..."
target = open(filename, 'w')
# Update user and truncate file.
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
#Prompt user to define three lines of text to add to target
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
#writes the following lines on lines 1, 2, and 3 of the text.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "and finally, we close it."
target.close()
