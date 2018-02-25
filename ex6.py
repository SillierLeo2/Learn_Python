# A string is usually a bit of text you want to display to someone or "export" out of the program you are writing.
# A string may countain a lot of variables, just remember to set a = on the variable.
# A string always need to have a " " ou ' ' to show python that you want it to be displayed.

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False # Variable with a true ou false value, displayable by {} without fulfilling it.
joke_evaluation = "Isn't that joke funny?! {}" # Variable with a {} to receive the other variable above. 

print(joke_evaluation.format(hilarious)) 

w = "This is the left side of..."
e = "a string with a right side."

print(w + e) # Two variables with a + that created a bigger one, such as a addiction itself.