#import argv and exists features.
from sys import argv ; from os.path import exists
script, from_file, to_file = argv
print "Copying from %s to %s" % (from_file, to_file)
# define indata as contents of opened from_file
indata = open(from_file).read()
# read and print the length of indata
# check if to_file exists, prompt user to quit/continue.
print "the input file is %d bytes long" % len(indata), "\n", "does the output file exist? %r" % exists(to_file), "\n", "Ready, hit RETURN to continue, CTRL-C to abort." ; raw_input()
# define out_file by opening to_file, make writeable, write.
out_file = open(to_file, 'w').write(indata) ; print "Done."
