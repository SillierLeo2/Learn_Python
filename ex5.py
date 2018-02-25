# A string is how you make something that your program might give to a human
# If you don't use a f before the "" it won't understand that will be a variable on it.
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age} , {my_height} , and {my_weight} I get {total}.")


name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 * 2.54 # inches
weight = 180 * 0.45  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} cm tall.")
print(f"He's {weight} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age} , {height} , and {weight} I get {total} ")
