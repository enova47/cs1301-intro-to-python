mystery_string = "ABCDE"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#In the example above, we saw using operators to add
#characters to the end of a string, and using operators to
#multiply a string.
#
#Add some code below that uses those operators to modify
#mystery_string such that its value at the end of the
#program is: ABCDE.ABCDE.ABCDE.??? Then, print the final
#value of mystery_string.
#
#You should not create any new strings longer than one
#character. We'll test your code with a couple other
#variants on mystery_string, but in all cases the results
#should be the same: the string repeated three times with
#a period after each repetition and three question marks
#at the end.


#Add your code here!
print(mystery_string + '.' + mystery_string + '.' + mystery_string + '.' + ("?" * 3))