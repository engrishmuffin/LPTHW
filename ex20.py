from sys import argv

script, input_file = argv
# print_all reads a document and prints it to the console
def print_all(f):
    print f.print_all
# rewind sets the reader back to the beginning of a document
def rewind(f):
    print f.seek(0)
# print a line prints the currently observed line preceded by its line number.
def print_a_line(line_count, f):
    print line_count, f.readline()
#defines current_file as the file opened with argv
current_file = open(input_file)

print "First let's print the whole file:\n"
# runs print_all on current_file
print_all(current_file)

print "now let's rewind, kind of like a tape."
# runs rewind on current_file
rewind(current_file)

print "Let's print three lines:"
# sets current_line to the first line in current_file
current_line = 1
# Runs print_a_line on current_line
print_a_line(current_line, current_file)
# moves current_line to the next line in the doc and runs print_a_line
current_line = current_line + 1
print_a_line(current_line, current_file)
# moves current_line to the next line in the doc and runs print_a_line again
current_line = current_line +1
print_a_line(current_line, current_file)
