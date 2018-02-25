formatter = "{} {} {} {}" #a string with 4 variables that will be defined on the next code lines;

print(formatter.format(1, 2, 3, 4)) 
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter)) # Each "formattter" brings {} with it, and in the end you have 16 on this line;
print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a poem",
	"Or a song about fear"
	))

#When you use {} on a string you may complete it using a .format and () to atribute the values;