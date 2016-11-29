name = 'Caedmon B. Webb'
age = 31 #not a lie
height = 72 #inches
weight = 193 #lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'
meters = height * 2.54
kilos = weight / 2.24

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "That's %d centimeters." % meters
print "He's %d pounds heavy." % weight
print "Or %d kilograms." % kilos
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usuall %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right.
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
