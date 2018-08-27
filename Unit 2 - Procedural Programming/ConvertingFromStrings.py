#In the code below, three strings are created. Only one can be
#converted to all three data types we're covering here (integers,
#floats, and booleans). Create three new variables called
#as_integer, as_float, and as_boolean, select the only variable
#that can be converted to all three, and convert it.
#
#Hint: Python lets you convert anything to a boolean. It
#interprets any non-empty string or non-zero number as True, and
#any empty string or number 0 as False.

a = "5.1"
b = "Hello!"
c = "5"

#Add your code here!
as_integer = int(c)
as_float = float(c)
as_boolean = bool(c)



#The lines of code below will test your submission! If it's
#working, it will print the value three times, followed by three
#different types: <class 'int'>, <class 'float'>, and
#<class 'bool'>.
print(as_integer, type(as_integer))
print(as_float, type(as_float))
print(as_boolean, type(as_boolean))