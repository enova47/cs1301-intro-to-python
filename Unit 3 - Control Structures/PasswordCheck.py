entered = "abc123"
password = "abc123"
tries = 3

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Above we've created three variables representing an attempt
#to enter a password. Add some code below that will print the
#result of this check:
#
# - "Login successful." if entered is the same as password
#   and tries is less than or equal to 3.
# - "Incorrect password." if entered is not the same as
#   password, but tries is less than or equal to 3.
# - "Tries exceeded." if tries is greater than 3.
#
#You don't need to worry about incrementing tries if the
#password is incorrect.


#Add your code here!
if tries <= 3:
    if entered == password:
        print("Login successful.")
    else:
        print("Incorrect password.")
elif tries > 3:
    print("Tries exceeded.")