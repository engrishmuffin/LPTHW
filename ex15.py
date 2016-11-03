from sys import argv
#prompts user to name the file they would like opened.
script, filename = argv
#defines txt by opening the file defined in the argv
txt = open(filename)
#prints the name of the file, and reads the opened txt.
print "Here's your file %r:" % filename
print txt.read()
#runs user through same process,
#this time asking for the filename within the program
print "type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
