#  The format specifier is a string that defines how a value should be formatted when it is converted
#  to a string. Format specifiers are commonly used in string formatting operations, allowing you to
#  control the appearance of numbers, strings and other data types when they are represented as strings.
#  Format specifiers are used in the format() function and in the string formatting operator %.
#  Format specifiers can be used to format numbers, strings, and other data types.


# .(number)f round to that many decimal places (fixed point)
# : (number) allocate that many spaces
# :03 allocate and zero pad that many spaces
# :<= left justify
# :> = right justify
# :^ = center align
# :+= use a plus sign to indicate positive value
# := = place sign to leftmost position
# : insert a space before positive numbers
# , comma separator

price1 = 10555.64135086
price2 = -24845.55086
price3 = 21250.589525

print(f"The price1 is ${price1:+,.2f}")
print(f"The price2 is ${price2:+,.2f}")
print(f"The price3 is ${price3:+,.3f}")