mystery_value = -1

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Notice that when you run this code, you encounter an error.
# Instead of this error, we want this code to print "Boo :("
# (without the quotes) if mystery_value is not greater than 0.
#
# Fix this error WITHOUT modifying the existing code. You can
# fix this error by only adding some code before the existing
# code below.


# Make any changes or additions here!
if mystery_value < 0:
    result = "Boo :("

# Don't change any of the code below!
if mystery_value > 0:
    print("mystery_value is greater than 0.")
    result = "Yay!"
else:
    print("mystery_value is less than 0.")

print(result)