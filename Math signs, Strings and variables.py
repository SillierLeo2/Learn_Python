+ plus #addiction
- minus #subtraction
/ slash #division
* asterisk #multiplication
% percent #modulus
< less-than #If the value of left operand is less than the value of right operand, then condition becomes true.
> greater-than #If the value of left operand is greater than the value of right operand, then condition becomes true.
<= less-than-equal #If the value of left operand is less than or equal to the value of right operand, then condition becomes true.
>= greater-than-equal #If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.
** double-asterisk #exponent

#how to use a String formatters 
# can't forget to use the {}

print("something that you wanna say {}.".format("plus something")) 

something = "Something that you wanna say"
print(something.format("plus something"))

# When using a specific variable, use f before the ""
types_of_people = 10
x = f"There are {types_of_people} types of people."
print(x)