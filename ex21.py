#defines "add" function, adds two variables
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b



print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "that becomes: ", what, "Can you do it by hand?"
def answer(a, b, c, d):
    print "Calculating %d - %d * %d / %d." (a, b, c, d)
    return a - b * c / d

# def answer(a, b, c, d):
#     print "Calculating %d - %d * %d / %d." (a, b, c, d)
#     return a - b * c / d
answer = age - (74 * height * (weight / iq))

print "the answer is ", answer, ". Pretty neat, huh?"
