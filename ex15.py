from sys import argv
# prompts user to name the file they would like opened.
script, filename = argv
# defines txt by opening the file(name) defined in the argv
txt = open(filename)
# prints the name of the file, and reads the opened txt.
print "Here's your file %r:" % filename
print txt.read()
# closes txt, which was defined by opening the file.
txt.close();
# runs user through same process,
# this time asking for the filename within the program
print "type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
# closes the opened file which was used to define txt_again.
txt_again.close();
# the next line should cause an error, because txt_again is closed.
# print txt_again.read()
# it DID, it DID cause an error!!!
