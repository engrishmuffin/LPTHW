print "Please answer all questions on a scale of 1-7."

print "How ambitious are you?"
amb = int(raw_input ())
print "How charitable are you?"
cha = int(raw_input ())
print "How much do you enjoy outsmarting people?"
out = int(raw_input ())
print "How much do you enjoy seeing others succeed?"
sup = int(raw_input ())
print "How much do you like to have others protect you?"
dfn = int(raw_input ())
print "How much do you like money?"
frm = int(raw_input ())
print "How much do you want to have an immediate impact?"
rly = int(raw_input ())
print "How much do you want to bear the most responsibility in a project?"
res = int(raw_input ())

print "Your support score is %r" % (cha + sup + out + rly)
print "Your carry score is %r" % (amb + frm + dfn )
