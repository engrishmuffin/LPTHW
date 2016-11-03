from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)
# define indata as contents of opened from_file
# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()
# read and print the length of indata
print "the input file is %d bytes long" % len(indata)
# check if to_file exists, prompt user to quit/continue.
print "does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()
# define out_file by opening to_file, make writeable, write.
out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
