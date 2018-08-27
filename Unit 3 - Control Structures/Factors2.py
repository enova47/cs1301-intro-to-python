mystery_int_1 = 15
mystery_int_2 = 5

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Remember the code we wrote in the last exercise? Let's
#modify it!
#
#Previously, you printed "Factors!" if one factor was a
#factor of the other. Now, add to that code: you should still
#print "Factors!" if one number is a factor of the other, but
#also print "Not factors :(" if neither number is a factor of
#the other.


#Add your code here! You can feel free to copy/paste your
#code or the exemplary answer from last exercise.
if mystery_int_1 % mystery_int_2 == 0 or mystery_int_2 % mystery_int_1 == 0:
    print("Factors!")
else:
    print("Not factors :(")