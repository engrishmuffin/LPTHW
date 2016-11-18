#copying example code for dealing with quotes inside strings
print "I am 6'2\" tall." #escape double-quote inside string
print 'I am 6\'2" tall.' #escape single-quote inside string

#use '\t to indent/tab in'
tabby_cat = "\tI'm tabbed in."
#use '\n to make a new line'
persian_cat = "I'm split\non a line."
#use double-backslash to, well, I dunno yet.
backslash_cat = "I'm \\ a \\ cat." #print backslashes, duh.

#use 3 double-quotes to do whatever you want.
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

#print the cats
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
