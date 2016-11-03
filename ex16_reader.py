from sys import argv

script, filename = argv

txt = open(filename)

print "This is the contents of %r:" % (filename)
print txt.read()
txt.close()
