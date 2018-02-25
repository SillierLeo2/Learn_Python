# a variable is a way to rename something that was already named before, as example: Renato may be a variable for "the one which coded this file"
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

#the first time I runned this program I had an error because the phrase on the line 3 and the one on the line 8 wasn't matching, so I rewrote the lines to match them.
#We may use a floating number on space in a car because space doen't need to be a complete number, we're working with capacity, not humans. In addiction, you may hit decimal numbers using the floating point.
# the equal symbol is used to show something value or represent a operation to get the variant value.
