mystery_int_1 = 15
mystery_int_2 = 5

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#The variables below hold two integers, mystery_int_1 and
#mystery_int_2. Complete this program below such that it
#prints "Factors!" if either of the numbers is a factor of
#the other. If neither number is a factor of the other,
#do not print anything.
#
#Hint: You can do this with just one conditional statement
#by using the logical expressions we learned earlier (and,
#or, and not). You'll also use the modulus operator we
#learned in Chapter 2.4.


#Add your code here!
if mystery_int_1  % mystery_int_2 == 0 or mystery_int_2 % mystery_int_1 == 0:
    print("Factors!")