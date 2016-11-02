# defines the formatter as a string series of four variables
formatter = "%r %r %r %r"

#defines formatter variables as Numbers: 1, 2, 3, 4
print formatter % (1, 2, 3, 4)
#defines formatter variables as strings
print formatter % ("one", "two", "three", "four")
#defines formatter as boolean variables
print formatter % (True, False, False, True)
#defines formatter as "formatter"
print formatter % (formatter, formatter, formatter, formatter)
#defines formatter as a series of longer strings.
print formatter % (
"I had this thing.",
"That you could type up right.",
"But it didn't sing.",
"So I said goodnight."
)
